from fastapi import FastAPI
from app.routes import movies

app = FastAPI()

app.include_router(movies.router, prefix="/api/movies")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Mood Movie Recommender API"}
