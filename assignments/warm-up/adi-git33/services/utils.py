from datetime import datetime

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
    
    if date and not hour and date not in data:
        return filtered_data

    for news_date in data:
        if date and not hour and news_date == date:
            filtered_data = {news_date: data[news_date]}
            
        if hour:    
            news_list = data[news_date]
            for news_obj in news_list:
                if hour in news_obj:
                    if date and news_date == date:
                        filtered_data = news_obj[hour]
                    else:
                        filtered_data = {news_date : news_obj[hour]}

    return filtered_data
                                        