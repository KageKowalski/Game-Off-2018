# -*- coding: utf-8 -*-


import enum


#Current location of the player
class Location(enum.Enum):
    HUB = 1
    ORBS = 2
    ASTEROIDS = 3
    PYXTRIP = 4
    TEMPLATE = 100


#Game state
class GameState(enum.Enum):
    GAME_START=0
    IN_PROGRESS=1
    GAME_OVER=2

