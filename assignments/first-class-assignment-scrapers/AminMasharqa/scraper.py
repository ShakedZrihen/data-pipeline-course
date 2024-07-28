import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

def scrape_ynet():
    url = "https://www.ynetnews.com/category/3089"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all elements with the specified class
    news_items = soup.find_all("div", class_="titleRow")
    
    # Dictionary to store the news items by hours
    news_dict = {}

    # Iterate over each news item
    for item in news_items:
        # Initialize variables to store date and title
        date_str = ""
        title = ""

        # Iterate over the children of the item
        for child in item.children:
            if child.name == "div" and "date" in child.get("class", []):
                # Extract the datetime attribute
                time_element = child.find("time")
                if time_element and time_element.has_attr("datetime"):
                    date_str = time_element["datetime"]
            elif child.name == "div" and "title" in child.get("class", []):
                # Extract the title text
                title = child.text.strip()

        # If date_str and title are found, process them
        if date_str and title:
            # Convert the datetime string to a datetime object
            news_time = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
            # Extract the full datetime
            news_full_datetime = news_time.strftime("%Y-%m-%d %H:%M:%S")
            # Add to the dictionary
            news_dict[news_full_datetime] = title

    # Sort the dictionary by keys (datetime) in descending order
    sorted_news_dict = dict(sorted(news_dict.items(), key=lambda item: item[0], reverse=True))

    # Save the sorted dictionary to a JSON file
    with open("2024-07-28.json", "w") as json_file:
        json.dump(sorted_news_dict, json_file, indent=4)

if __name__ == "__main__":
    scrape_ynet()
