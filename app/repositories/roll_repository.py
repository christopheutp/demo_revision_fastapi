"""Stockage en mémoire : remplaçable ultérieurement par une base de données."""


class RollRepository:
    def __init__(self):
        self._rolls = []  # Le préfixe _ signale un détail interne (convention Python).
        self._next_id = 1

    def save(self, sides, result):
        record = {"id": self._next_id, "sides": sides, "result": result}
        self._rolls.append(record)
        self._next_id += 1
        return record.copy()  # Évite de donner accès au dictionnaire stocké.

    def list_all(self):
        return [record.copy() for record in self._rolls]

    def count(self):
        return len(self._rolls)

    def total(self):
        return sum(record["result"] for record in self._rolls)
