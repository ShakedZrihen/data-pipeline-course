import requests

def get_all_events_test():
    url = "http://localhost:3000"
    res = requests.get(url)
    data = res.json()
    assert res.status_code == 200
    assert res.headers["Content-Type"] == "application/json; charset=UTF-8"
    assert isinstance(data, dict)
    
def get_day_events_test():
    url = "http://localhost:3000?date=27/07/2024"
    res = requests.get(url)
    data = res.json()
    assert res.status_code == 200
    assert res.headers["Content-Type"] == "application/json; charset=UTF-8"
    assert isinstance(data, dict)
    
def day_wrong_format_test():
    url = "http://localhost:3000?date=27/07.2024"
    res = requests.get(url)
    assert res.status_code == 400
    
def get_hour_event_test():
    url = "http://localhost:3000?time=05:59"
    res = requests.get(url)
    data = res.json()
    assert res.status_code == 200
    assert res.headers["Content-Type"] == "application/json; charset=UTF-8"
    assert isinstance(data, dict)
    
def hour_wrong_format_test():
    url = "http://localhost:3000?time=05%359"
    res = requests.get(url)
    assert res.status_code == 400