"""Couche HTTP : elle traduit les requêtes en appels au service."""

from fastapi import APIRouter, Depends, HTTPException

from app.dependencies import get_dice_service
from app.schemas.roll import RollRequest, RollResponse, StatsResponse

# APIRouter regroupe des endpoints, séparément de la création de l'application.
router = APIRouter(tags=["Dés"])


# Un décorateur @router.post associe la fonction à POST /rolls.
# response_model indique à FastAPI le schéma des données retournées.
@router.post("/rolls", response_model=RollResponse, status_code=201)
def create_roll(data: RollRequest, service=Depends(get_dice_service)):
    # "data: RollRequest" : FastAPI lit et valide automatiquement le JSON.
    # Depends(...) : FastAPI fournit le service, sans qu'on le crée ici.
    try:
        return service.roll(data.sides)
    except ValueError as error:
        # HTTPException traduit une erreur métier en réponse HTTP 400.
        raise HTTPException(status_code=400, detail=str(error)) from error


@router.get("/rolls", response_model=list[RollResponse])
def get_rolls(service=Depends(get_dice_service)):
    # list[RollResponse] : la réponse est une liste d'objets RollResponse.
    return service.history()


@router.get("/stats", response_model=StatsResponse)
def get_stats(service=Depends(get_dice_service)):
    return service.stats()
