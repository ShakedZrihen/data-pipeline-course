from datetime import datetime
from fastapi import HTTPException

def validate_input(input, input_format):
    if input:
        try:
            res = bool(datetime.strptime(input, input_format))
            return res
        except ValueError:
            return False
    else:
        return True

    
def filter_data(data, date, hour):
    filtered_data = {}
    for news_date in data:
        if date and news_date == date:
            filtered_data = {news_date: data[news_date]}
            
        news_list = data[news_date][0]
        if hour and any(news == hour for news in news_list):
            if date:
                filtered_data = news_list[hour]
            else:
                filtered_data = {news_date : news_list[hour]}
    return filtered_data
                                        