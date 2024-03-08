import requests
from bs4 import BeautifulSoup

def get_links_from_url(url):
    try:
        # Fetch the webpage content
        response = requests.get(url)
        # Check if request was successful
        if response.status_code == 200:
            # Parse the HTML content
            soup = BeautifulSoup(response.content, 'html.parser')
            # Find all the links on the page
            links = []
            for link in soup.find_all('a'):
                href = link.get('href')
                if href:
                    links.append(href)
            return links
        else:
            print("Failed to fetch the webpage. Status code:", response.status_code)
            return None
    except Exception as e:
        print("An error occurred:", e)
        return None

# Prompt the user for a URL
url = input("Enter the URL: ")

# Call the function to get links from the provided URL
links = get_links_from_url(url)
if links:
    print("Links found on", url, ":")
    for link in links:
        print(link)
