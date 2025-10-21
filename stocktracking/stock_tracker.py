# Simple Stock Tracker

# Step 1: Define stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "AMZN": 135,
    "GOOGL": 140,
    "MSFT": 330
}

# Step 2: Collect user input
portfolio = {}
while True:
    stock = input("Enter stock name (or 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Stock not found in database. Try again.")
        continue
    try:    
        quantity = int(input(f"Enter quantity for {stock}: "))
        portfolio[stock] = quantity
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Step 3: Calculate total investment
total_investment = 0
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    investment = price * qty
    print(f"{stock}: {qty} × ${price} = ${investment}")
    total_investment += investment

print(f"\nTotal Investment Value: ${total_investment}")

# Step 4: Save results to csv file
save = input("Save results to file? (yes/no): ").lower()
try:
    if save == "yes":
        with open("stock_investment.csv", "w") as file:
            file.write("Stock,Quantity,Price,Investment\n")
            for stock, qty in portfolio.items():
                price = stock_prices[stock]
                investment = price * qty
                file.write(f"{stock},{qty},{price},{investment}\n")
            file.write(f"\nTotal,,,{total_investment}\n")
        print("Results saved to 'stock_investment.csv'")
    else:
        print('Your results has not been saved')
except Exception as e:
    print(f"An unexpected error occurred: {e}")
