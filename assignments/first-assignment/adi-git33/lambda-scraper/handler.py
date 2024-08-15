from fastapi import FastAPI
from mangum import Mangum
from routers.router import router 
import uvicorn

app = FastAPI()
app.include_router(router)
handler = Mangum(app)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080, reload=True)
