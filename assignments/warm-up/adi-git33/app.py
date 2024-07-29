from fastapi import FastAPI
from routers.router import router 
import uvicorn

app = FastAPI()

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)

# uvicorn main:app --reload --port 8000