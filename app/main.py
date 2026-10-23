"""Point d'entrée de l'application FastAPI."""

from fastapi import FastAPI
from app.routers.rolls import router as rolls_router

app = FastAPI(title="Dice Lab API", version="1.0.0")


# Décorateur : associe une fonction Python à une route HTTP.
@app.get("/")
def welcome():
    return {"message": "Bienvenue dans Dice Lab", "docs": "/docs"}


# On rattache toutes les routes déclarées dans le module rolls.py.
app.include_router(rolls_router)
