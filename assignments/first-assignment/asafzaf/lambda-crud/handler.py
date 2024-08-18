from fastapi import FastAPI, HTTPException
from mangum import Mangum
import logging

logging.basicConfig(level=logging.INFO)

app = FastAPI()

@app.get("/health")
def health():
    try:
        return 200
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error!")
    
    
handler = Mangum(app)