import os
import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

url = 'https://www.ynet.co.il/news/category/184'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

all_news = soup.find_all('div', class_='titleRow')
all_titles = [news.find('div', class_='title').text.strip() for news in all_news]

data = {}

try:
    driver.get(url)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'DateDisplay'))
    )

    time_elements = driver.find_elements(By.CLASS_NAME, 'DateDisplay')

    for time_element, title in zip(time_elements, all_titles):
        displayed_time = time_element.text.strip()
        data[displayed_time] = title

finally:
    driver.quit()

todays_date = datetime.now().strftime('%Y-%m-%d') # yyyy-mm-dd
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, f'{todays_date}.json')

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
