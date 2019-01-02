import random

ROLLS = ["rock", "paper", "scissors"]


class Player:

    def __init__(self, name):
        self.name = name


class Roll:
    def __init__(self):
        self.roll = random.choice(ROLLS)
        self.wins = self._wins_against()
        self.lose = self._lose_against()

    def _wins_against(self):
        if self.roll == "rock":
            return "scissors"
        if self.roll == "paper":
            return "rock"
        if self.roll == "scissors":
            return "paper"

    def _lose_against(self):
        if self.roll == "rock":
            return "paper"
        if self.roll == "paper":
            return "scissors"
        if self.roll == "scissors":
            return "rock"

    def can_defeat(self, opponent):
        return self.wins == opponent.roll
