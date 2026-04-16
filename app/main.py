from fastapi import FastAPI
from app.routes import ad, game

app = FastAPI()

app.include_router(ad.router)
app.include_router(game.router)

@app.get("/")
def root():
    return {"msg": "AdPlay Engine Running"}
