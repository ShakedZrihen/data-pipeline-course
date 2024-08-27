from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Ensures Chrome runs headless
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")  # Applicable if running in Docker
chrome_options.add_argument("--remote-debugging-port=9222")  # port for debug

# Automatically download and set up ChromeDriver
service = Service(ChromeDriverManager().install())

# Set up WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)


def download_wikipedia_pages(query):
    # Navigate to Wikipedia
    driver.get("https://en.wikipedia.org/wiki/Lady_Gaga")

    # Ensure a directory for saving HTML files
    if not os.path.exists(query):
        os.makedirs(query)

    # Find all <p> tags
    paragraphs = driver.find_elements(By.TAG_NAME, "p")

    # Print all paragraphs to log
    for paragraph in paragraphs:
        print(paragraph.text)

    # save all paragraphs to a file
    with open(f"{query}/all_paragraphs.txt", "w") as file:
        for paragraph in paragraphs:
            file.write(paragraph.text + "\n")

    print("Download complete.")


# Download all Wikipedia pages related to Lady Gaga
download_wikipedia_pages("Lady Gaga")

# Close the driver
driver.quit()
