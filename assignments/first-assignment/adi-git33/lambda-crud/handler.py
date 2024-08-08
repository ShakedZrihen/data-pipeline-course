from fastapi import FastAPI
from mangum import Mangum
import uvicorn

app = FastAPI()
handler = Mangum(app)

@app.get("/health")
async def root():
    return {"message": "App is running"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)

