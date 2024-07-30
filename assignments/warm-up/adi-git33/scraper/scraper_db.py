from scraper.ynet_scraper import scrape_ynet
import json
import os
from datetime import date

def scrap_data(file_name):
    data = []
    today = date.today()
    formatted_today = str(today.strftime("%d/%m/%Y"))
    with open(file_name, 'r', encoding='utf-8') as f:
        data = json.load(f)
    check_date = False
    
    for news_date in data:
        if formatted_today == news_date:
            check_date = True
            
    if not check_date:
        scrape_ynet()
            

class Database:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Database, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        if hasattr(self, '_initialized') and self._initialized:
            return
        
        file_path = os.path.split(os.path.realpath(__file__))[0]
        file_name = file_path + '/news.json'
        self.db = file_name
        scrap_data(file_name)

    def get_data(self):
        try:
            data = []
            with open(self.db, 'r', encoding='utf-8') as f:
                data = json.load(f)
            return data
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            raise