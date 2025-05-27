from fastapi import FastAPI
from app.routes import image_routes, moondream_routes
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.include_router(image_routes.router)
app.include_router(moondream_routes.router)

@app.get("/")
def root():
    return {"message": "Moondream API is running"} 