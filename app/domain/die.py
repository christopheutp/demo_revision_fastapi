"""Objet métier : un dé de jeu, indépendant de FastAPI."""

import random


class Die:
    def __init__(self, sides):
        # self désigne l'instance créée ; chaque dé conserve son nombre de faces.
        if sides < 2:
            raise ValueError("Un dé doit posséder au moins 2 faces")
        self.sides = sides

    def roll(self):
        # randint(a, b) tire un entier aléatoire entre a et b, bornes incluses.
        return random.randint(1, self.sides)
