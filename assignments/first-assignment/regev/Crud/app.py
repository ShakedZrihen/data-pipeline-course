import logging
from fastapi import FastAPI 
from mangum import Mangum


# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


app = FastAPI(
    title="Breaking News API",
    description="An API to fetch breaking news based on date and time.",
    version="1.0.0"
)

@app.get("/health", summary="Health Check", description="Check the health status of the API")
def health():
    logger.info("Health endpoint called")
    return {"status": "ok"}




handler = Mangum(app)
