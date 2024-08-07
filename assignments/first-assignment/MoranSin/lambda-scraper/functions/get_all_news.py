import json
import os

def get_all_news():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'data-raw-q.json')
    with open(file_path, encoding='utf-8') as f:
        data = json.load(f)  
    return data
    