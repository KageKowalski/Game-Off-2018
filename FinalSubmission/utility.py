# -*- coding: utf-8 -*-


import enum


#Current location of the player
class Location(enum.Enum):
    HUB = 1
    ORBS = 2
    ASTEROIDS = 3
    TEMPLATE = 100

