# -*- coding: utf-8 -*-


#imports
import pyxel
import utility
import Hub
import Orbs
import Template
import Asteroids
import PyxTrip


#Game application which is run in run.py
class App:
    #Initialize pyxel
    #Load resources
    #Initialize games
    #Run pyxel
    def __init__(self):
        pyxel.init(192,128,caption="RetroHub")
        pyxel.load("resources.pyxel")
        self.hub=Hub.Hub()
        self.orbs=Orbs.Orbs()
        self.template=Template.Template()
        self.asteroids=Asteroids.Asteroids()
        self.pyxtrip=PyxTrip.PyxTrip()
        self.location=utility.Location.HUB
        pyxel.run(self.update,self.draw)
    
    
    #Update App based on Player Location
    def update(self):
        #Exit RetroHub
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()
        
        #Update Hub
        if self.location==utility.Location.HUB:
            self.location=self.hub.update()
        #Update Template
        elif self.location==utility.Location.TEMPLATE:
            if self.template.update():
                self.location=utility.Location.HUB
                self.hub.player.pyx += self.template.getPyx()
                self.template=Template.Template()
        #Update Orbs
        elif self.location==utility.Location.ORBS:
            if self.orbs.update():
                self.location=utility.Location.HUB
                self.hub.player.pyx += self.orbs.getPyx()
                self.orbs=Orbs.Orbs()
        #Update Asteroids
        elif self.location==utility.Location.ASTEROIDS:
            if self.asteroids.update():
                self.location=utility.Location.HUB
                self.hub.player.pyx += self.asteroids.getPyx()
                self.asteroids=Asteroids.Asteroids()
        #Update PyxTrip
        elif self.location==utility.Location.PYXTRIP:
            if self.pyxtrip.update():
                self.location=utility.Location.HUB
                self.hub.player.pyx += self.pyxtrip.getPyx()
                self.pyxtrip=PyxTrip.PyxTrip()
    
    
    #Draw App based on Player Location
    def draw(self):
        #Draw Hub
        if self.location==utility.Location.HUB:
            self.hub.draw()
        #Draw Template
        elif self.location==utility.Location.TEMPLATE:
            self.template.draw()
        #Draw Orbs
        elif self.location==utility.Location.ORBS:
            self.orbs.draw()
        #Draw Asteroids
        elif self.location==utility.Location.ASTEROIDS:
            self.asteroids.draw()
        #Draw PyxTrip
        elif self.location==utility.Location.PYXTRIP:
            self.pyxtrip.draw()

