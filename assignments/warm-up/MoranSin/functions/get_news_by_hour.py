from functions.get_all_news import get_all_news 

def news_by_hour(hour):
    data = get_all_news()
    # for date in data:
    print("date: ",hour)
    hours_data += data[hour]
    return hours_data