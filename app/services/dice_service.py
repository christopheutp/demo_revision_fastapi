"""Couche service : règles de l'application, sans connaissance du protocole HTTP."""

from app.domain.die import Die


class DiceService:
    def __init__(self, repository):
        # Injection par constructeur : le service reçoit son stockage de l'extérieur.
        self.repository = repository

    def roll(self, sides):
        if sides not in (6, 12, 20):
            raise ValueError("Seuls les dés à 6, 12 et 20 faces sont autorisés")
        die = Die(sides)
        return self.repository.save(sides, die.roll())

    def history(self):
        return self.repository.list_all()

    def stats(self):
        count = self.repository.count()
        # Évite une division par zéro si aucun lancer n'a encore été effectué.
        average = self.repository.total() / count if count else None
        return {"roll_count": count, "average_result": average}
