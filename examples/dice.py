"""Dice throw modeling."""
from random import randint


class Dice:
    """Class to describe dice."""

    def __init__(self, num_sides=6):
        """Six-sides dice by default."""
        self.num_sides = num_sides

    def roll(self):
        """Return random side."""
        return randint(1, self.num_sides)
