from fastapi import FastAPI
from mangum import Mangum
from routers.router import router 
import uvicorn

app = FastAPI()
app.include_router(router)
handler = Mangum(app)
