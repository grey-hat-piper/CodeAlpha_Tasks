# Webpage title scrapper
import requests
import re

# Fetching title function
def fetch_web(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        # Extract the title from HTML using regex
        match = re.search(r"<title>(.*?)</title>", response.text, re.IGNORECASE | re.DOTALL)
        if match:
            title = match.group(1).strip()
            return title
        else:
            print("No <title> found in the webpage.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching: {e}")
        print("Input the correct URL or check your connection!")

title =None
# User URL input
while title ==None or url =="done".lower():
    url = input('Enter your URL (or \'done\' to EXIT):')
    if url =="done".lower():
        exit()
    print('Scraping web...')    
    title= fetch_web(url)
    
    if title !=None:
        print(f"Title is:{title}")
        


# Write in file
if title is not None:
    with open('title.txt','a') as file:
        file.write(f"Website:{url}\nTitle:{title}\n")
    print(f'Title successfully saved to title.txt')