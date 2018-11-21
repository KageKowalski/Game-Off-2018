# -*- coding: utf-8 -*-


#imports
import pyxel
import random
import math


#Orbs game
class Orbs:
    #Ball entity
    class Ball:
        def __init__(self,_v=(random.random(),random.random()),_x=float(10),_y=float(10),_r=4,_c=random.randint(1,15)):
            self.x = _x
            self.y = _y
            self.r = _r
            self.v = _v
            self.c = _c
    
    
    #Paddle entity (Player cursor)
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
    
    
    #Initialize balls list (and first Ball)
    #Initialize score
    #Initialize Paddle
    def __init__(self):
        self.balls = [self.Ball((random.random()+0.5,random.random()+0.5))]
        self.score = 0
        self.paddle = self.Paddle(0,0)
    
    
    #Update Orbs
    def update(self):
        #Return to Hub if Player presses 'B' key
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
    
    
    #Draw Orbs
    def draw(self):
        #Clear screen
        pyxel.cls(0)
        
        #Draw Paddle
        pyxel.rect(self.paddle.x-self.paddle.hl,self.paddle.y-self.paddle.hl,self.paddle.x+self.paddle.hl,self.paddle.y+self.paddle.hl,self.paddle.c)
        
        #Draw Balls
        for ball in self.balls:
            pyxel.circ(ball.x,ball.y,ball.r,ball.c)
        
        #Print score
        pyxel.text(2,2,str(self.score),random.randint(1,15))

