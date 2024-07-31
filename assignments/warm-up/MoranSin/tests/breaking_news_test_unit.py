import requests

def test_get_all_events():
    url = "http://localhost:3000/breaking-news"
    res = requests.get(url)
    data = res.json()
    assert res.status_code == 200
    assert isinstance(data, dict)
    
def test_get_health():
    url = "http://localhost:3000/health"
    res = requests.get(url)
    assert res.status_code == 200
    
def test_get_day_events():
    url = "http://localhost:3000/breaking-news?date=27/07/2024"
    res = requests.get(url)
    assert res.status_code == 200

    
def test_day_wrong_format():
    url = "http://localhost:3000/breaking-news?date=27/5.5"
    res = requests.get(url)
    assert res.status_code == 400
    
def test_get_hour_event():
    url = "http://localhost:3000/breaking-news?time=05:59"
    res = requests.get(url)
    assert res.status_code == 200
    
def test_hour_wrong_format():
    url = "http://localhost:3000/breaking-news?time=5"
    res = requests.get(url)
    assert res.status_code == 400
    
def test_event_not_found():
    url = "http://localhost:3000/breaking_news?date=27/07/2024&time=5:59"
    res = requests.get(url)
    assert res.status_code == 404