# -*- coding: utf-8 -*-


import pyxel
import enum
import random
import math


#Game application which is run in run.py
class App:
    class Location(enum.Enum):
        HUB = 1
        ORBS = 2
    
    
    def __init__(self):
        pyxel.init(192,128,caption="RetroHub")
        pyxel.load("resources.pyxel")
        self.location=self.Location.HUB
        self.hub=Hub()
        self.orbs=Orbs()
        pyxel.run(self.update,self.draw)
    
    
    def update(self):
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()
        elif pyxel.btnp(pyxel.KEY_O):
            self.location=self.Location.ORBS
        
        if self.location==self.Location.HUB:
            self.hub.update()
        elif self.location==self.Location.ORBS:
            if self.orbs.update():
                self.location=self.Location.HUB
        
        
    def draw(self):
        pyxel.cls(0)
        
        if self.location==self.Location.HUB:
            self.hub.draw()
        elif self.location==self.Location.ORBS:
            self.orbs.draw()




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
    class Ball:
        def __init__(self,_v=(random.random(),random.random()),_x=float(10),_y=float(10),_r=4,_c=random.randint(1,15)):
            self.x = _x
            self.y = _y
            self.r = _r
            self.v = _v
            self.c = _c
    
    
    class Paddle:
        def __init__(self,_x,_y,_hl=3,_c=random.randint(1,15)):
            self.x = _x
            self.y = _y
            self.hl = _hl
            self.c = _c
            self.ulc = (self.x-self.hl,self.y-self.hl)
            self.urc = (self.x+self.hl,self.y-self.hl)
            self.llc = (self.x-self.hl,self.y+self.hl)
            self.lrc = (self.x+self.hl,self.y+self.hl)
    
    
    def __init__(self):
        self.balls = [self.Ball((random.random(),random.random()))]
        self.score = 0
        self.paddle = self.Paddle(0,0)
    
    
    def update(self):
        #Quit game if player presses escape key
        if pyxel.btnp(pyxel.KEY_B):
            return True
        
        #Handle Collisions
        for ball in self.balls:
            #Handle ball-window collisions
            if ball.x + ball.r >= 160 or ball.x - ball.r <= 0:
                ball.v = (-ball.v[0],ball.v[1])
            elif ball.y + ball.r >= 120 or ball.y - ball.r <= 0:
                ball.v = (ball.v[0],-ball.v[1])
            #Handle ball-paddle collisions
            elif math.sqrt( ((ball.x-self.paddle.ulc[0])**2)+((ball.y-self.paddle.ulc[1])**2) ) <= ball.r or math.sqrt( ((ball.x-self.paddle.urc[0])**2)+((ball.y-self.paddle.urc[1])**2) ) <= ball.r or math.sqrt( ((ball.x-self.paddle.llc[0])**2)+((ball.y-self.paddle.llc[1])**2) ) <= ball.r or math.sqrt( ((ball.x-self.paddle.lrc[0])**2)+((ball.y-self.paddle.lrc[1])**2) ) <= ball.r:
                ball.v = (-ball.v[0],-ball.v[1])
                self.score = self.score + 1
            
            #Move paddle and balls
            ball.x = ball.x + ball.v[0]
            ball.y = ball.y + ball.v[1]
        self.paddle = self.Paddle(pyxel.mouse_x,pyxel.mouse_y)
        
        return False
    
    
    def draw(self):
        #Clear screen
        pyxel.cls(0)
        
        #Draw paddle
        pyxel.rect(self.paddle.x-self.paddle.hl,self.paddle.y-self.paddle.hl,self.paddle.x+self.paddle.hl,self.paddle.y+self.paddle.hl,self.paddle.c)
        
        #Draw balls
        for ball in self.balls:
            pyxel.circ(ball.x,ball.y,ball.r,ball.c)
        
        #Print score
        pyxel.text(2,2,str(self.score),random.randint(1,15))


















