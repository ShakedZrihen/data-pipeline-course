from bs4 import BeautifulSoup
import requests
import json


def get_lecturers():
    url = "https://www.shenkar.ac.il/he/departments/סגל-המחלקה-להנדסת-תוכנה"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    lecturers_nodes = soup.find_all("article", class_="article employee-item")
    lecturer_object = {}

    for lecturer in lecturers_nodes:
        img = lecturer.find("img").get("data-lazy-src")
        additional_info = lecturer.find("div", class_="employee-item__content")
        name = additional_info.find("a").text
        title = additional_info.find("span").text
        lecturer_object[name] = {"title": title, "image": img}

    return lecturer_object


def save_lecturers_to_json(data):
    with open('lecturers.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


lecturers = get_lecturers()
save_lecturers_to_json(lecturers)
