"""Assemblage des objets : une instance partagée pour toute la démonstration."""

from app.repositories.roll_repository import RollRepository
from app.services.dice_service import DiceService

_repository = RollRepository()
_service = DiceService(_repository)


def get_dice_service():
    # FastAPI appellera cette fonction via Depends avant d'exécuter la route.
    return _service


def reset_demo_data():
    """Utile uniquement pour remettre à zéro le stockage dans les tests."""
    global _repository, _service
    _repository = RollRepository()
    _service = DiceService(_repository)
