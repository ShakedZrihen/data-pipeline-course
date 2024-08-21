from fastapi import FastAPI
from mangum import Mangum
import logging

app = FastAPI()

logger = logging.getLogger("health_check")
logger.setLevel(logging.INFO)

@app.get("/health")
def health_check():
    response = {"status": "healthy"}
    
    logger.info(f"Health check requested. Response: {response}")
    
    return response

handler = Mangum(app)
