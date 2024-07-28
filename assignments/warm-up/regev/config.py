import os

DB_FOLDER = os.path.join(os.path.dirname(__file__), 'resource')
os.makedirs(DB_FOLDER, exist_ok=True)