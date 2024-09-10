# WEB SCRAPER
#---------------------------------------------------
import requests   # Importing Requests Module
from bs4 import BeautifulSoup   # Importing Beautifulsoup Module
import csv

# URL of the ShadowFox website
url = "https://www.shadowfox.in/#"

# Custom exception for website access errors
class WebsiteAccessError(Exception):
    pass

# Function to send a GET request and handle errors
def fetch_url(url):
    try:
        print(f"Sending GET request to {url}")
        response = requests.get(url)
        print(f"Response status code: {response.status_code}")
        response.raise_for_status()  # Raise an exception for non-2xx status codes
        return response.text
    except requests.exceptions.RequestException as e:
        raise WebsiteAccessError(f"Error fetching URL: {e}")

# Function to extract data from the website
def extract_data(html_content):
    soup = BeautifulSoup(html_content, "html.parser")

    # Extract the desired data
    title = soup.find("title").text

    # Extract description and keywords from meta tags
    description_meta = soup.find("meta", {"name": "description"})
    description = description_meta["content"] if description_meta else None

    keywords_meta = soup.find("meta", {"name": "keywords"})
    keywords = keywords_meta["content"] if keywords_meta else None

    internship_titles = [h3.text for h3 in soup.select("section.internship h3")]

    return title, description, keywords, internship_titles

# Function to save data to a CSV file
def save_to_csv(data, filename):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Description", "Keywords", "Internship Titles"])
        writer.writerows(data)

# Fetch the website content
try:
    html_content = fetch_url(url)
    print("Website content fetched successfully")
    # Extract data if the website content was fetched successfully
    if html_content:
        title, description, keywords, internship_titles = extract_data(html_content)
        data = [(title, description, keywords, ", ".join(internship_titles))]
        save_to_csv(data, "scraped_data.csv")
        print("Data extraction completed and saved to scraped_data.csv")
    else:
        print("Failed to fetch website content.")
except WebsiteAccessError as e:
    print(f"Error: {e}")