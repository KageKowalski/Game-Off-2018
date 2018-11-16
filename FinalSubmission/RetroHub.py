# -*- coding: utf-8 -*-

import pyxel
import enum


class App:
    class Location(enum.Enum):
        HUB = 1
        ORBS = 2
    
    def __init__(self):
        pyxel.init(192,128,caption="RetroHub")
        pyxel.load("resources.pyxel")
        self.location=self.Location.HUB
        self.hub=Hub()
        pyxel.run(self.update,self.draw)
    
    def update(self):
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()
        
        if self.location==self.Location.HUB:
            self.hub.update()
        
    def draw(self):
        pyxel.cls(0)
        
        if self.location==self.Location.HUB:
            self.hub.draw()


class Hub:
    class Character:
        def __init__(self,_x,_y,_event=None):
            self.position = (_x,_y) #Coords of lower left pixel of block character is inhabiting
            self.event = _event #Event triggered by talking to this character
        
    def __init__(self):
        self.player = self.Character(pyxel.width/2,pyxel.height/2)
    
    def update(self):
        None
    
    def draw(self):
        pyxel.cls(0)
        pyxel.bltm(0,0,0,0,0,pyxel.width,pyxel.height)

class Orbs:
    def __init__(self):
        None
    
    def update(self):
        None
    
    def draw(self):
        None


















