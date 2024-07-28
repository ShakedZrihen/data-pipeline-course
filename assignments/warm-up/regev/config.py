import os

DB_FOLDER = os.path.join(os.path.dirname(__file__), 'db')
os.makedirs(DB_FOLDER, exist_ok=True)