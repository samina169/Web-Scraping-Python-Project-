import streamlit as st
import requests
from bs4 import BeautifulSoup

html_doc = """
<!DOCTYPE html>
<html>
<head>
<title>My Example Page</title>
</head>
<body>
<h1>Hello, World!</h1>
<p class="content">This is some text.</p>
<a href="https://example.com">Visit Example</a>
</body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

# Now you can use the 'soup' object to navigate and extract data
title = soup.title.string
print(title)  # Output: My Example Page

paragraph = soup.find('p', class_='content').text
print(paragraph)  # Output: This is some text.

link = soup.find('a')['href']
print(link)  # Output: https://example.com

def scrape_website(url):
    # Send a GET request to the specified URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the content of the page
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Example: Extract and print the title of the page
        title = soup.title.string
        print(f'Title of the page: {title}')
    else:
        print(f'Failed to retrieve the webpage. Status code: {response.status_code}')

if __name__ == "__main__":
    # Example URL to scrape
    url = 'https://example.com'
    scrape_website(url)
