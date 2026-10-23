"""Schémas HTTP : valider une demande et documenter les réponses."""

from pydantic import BaseModel, Field


# BaseModel (Pydantic) valide automatiquement les données JSON d'une requête.
class RollRequest(BaseModel):
    # ": int" est une annotation de type ; Field contrôle la validation.
    # strict=True refuse par exemple la chaîne JSON "6" à la place de 6.
    sides: int = Field(default=6, strict=True)


class RollResponse(BaseModel):
    # Ces annotations décrivent la forme de la réponse et apparaissent dans /docs.
    id: int
    sides: int
    result: int


class StatsResponse(BaseModel):
    roll_count: int
    # "float | None" signifie : nombre décimal OU valeur absente (null en JSON).
    average_result: float | None
