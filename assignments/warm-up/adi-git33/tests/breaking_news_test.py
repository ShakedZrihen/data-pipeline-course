import pytest
import requests
local_url = 'http://localhost:8000'

def get_response(params = {}):
    url = f"{local_url}/breaking-news"
    response = {}
    if params: 
        response = requests.get(url, params)
    else:
        response = requests.get(url)
    return response

# test for health
def test_get_health():
    url = f"{local_url}/health" 
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()  
    assert isinstance(data, dict)
    assert "message" in data

# test for breaking-news
def test_get_breaking_news():
    response = get_response()
    assert response.status_code == 200
    data = response.json()  
    assert len(data) > 0  


# test for breaking-news get by date
@pytest.mark.parametrize("date, status_code", [
    ('25/07/2024', 200),
    ('31/07/2024', 404),
])
def test_get_breaking_news_by_date(date, status_code):
    params = {'date' : date}
    response = get_response(params)
    assert response.status_code == status_code
    data = response.json()  
    assert len(data) > 0  
    

# test for breaking-news get by time
@pytest.mark.parametrize("time, status_code", [
    ('23:32', 200),
    ('11:11', 404),
])
def test_get_breaking_news_by_time(time, status_code):
    params = {'time' : time}
    response = get_response(params)
    assert response.status_code == status_code
    data = response.json()  
    assert len(data) > 0  
    
# test for breaking-news get by date and time
@pytest.mark.parametrize("date, time, status_code", [
    ('29/07/2024', '21:44', 200),
    ('29/07/2024', '21:00', 404),
    ('20/07/2024', '21:00', 404), 
])
def test_get_breaking_news_by_date_and_hour(date, time, status_code):
    params = {'date' : date, 'time' : time}
    response = get_response(params)
    assert response.status_code == status_code
    data = response.json()  
    assert len(data) > 0  