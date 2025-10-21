import random #for activating predefined words at random

#HANGMAN FUNCTION
def hangman():
    # List of predefined programming languages
    word_list = ['python', 'java', 'kotlin', 'javascript', 'rust', 'golang', 'rust', 'swift', 'typescript', 'ruby']
    
    # Randomly select a word from the list
    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)# Get the length of the chosen word
    
    # Create a display with underscores for each letter in the chosen word
    display = ['_'] * word_length
    guessed_letters = []# List to keep track of guessed letters
    attempts = 6  # Number of allowed incorrect attempts
    
    print("Welcome to Hangman!")
    print("Guess the PROGRAMMING LANGUAGE: " , ' '.join(display))
    print(f"You have {attempts} attempts remaining.\n")

    
    while attempts > 0 and '_' in display: # Continue until attempts run out or word is guessed
        guess = input("Please guess a letter: ").lower()
        
        # Input validation
        # Check if input is a single and alphabetical character
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single alphabetical character.\n")
            continue
        # Check if letter has already been guessed and is in the guessed_letters list
        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.\n")
            continue
        
        guessed_letters.append(guess)# Add the guessed letter to the list
        
        if guess in chosen_word: # Check if the guessed letter is in the chosen word
            for index, letter in enumerate(chosen_word): 
                if letter == guess:
                    display[index] = guess # Update the display with the correct guess
            print("Good guess!")
        else:
            attempts -= 1 # Decrement attempts for incorrect guess
            print(f"Wrong guess. You have {attempts} attempts remaining.")
        
        print(' '.join(display) + "\n") # Show the current state of the word
    if '_' not in display: # Check if the word has been completely guessed
        print("Congratulations! You've guessed the word correctly!")
    else: # If attempts run out
        print(f"Sorry, you've run out of attempts. The word was '{chosen_word}'.")
        print("Game Over.")

# Start the game
while True: # Loop to allow replaying the game
    hangman()
    play_again = input("Do you want to play again? (yes/no): ").lower() # Prompt to play again
    if play_again != 'yes': 
        print("Thank you for playing Hangman! Goodbye!") 
        break # Exit the loop if the player does not want to play again
    
