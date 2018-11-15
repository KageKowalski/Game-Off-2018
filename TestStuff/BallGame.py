# -*- coding: utf-8 -*-

import pyxel
import random
import math

#Balls which bounce around
class Ball:
    def __init__(self,_x=float(10),_y=float(10),_r=4,_v=(random.random(),random.random()),_c=random.randint(1,15)):
        self.x = _x
        self.y = _y
        self.r = _r
        self.v = _v
        self.c = _c

#Paddle which reflects balls
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

#Application
class App:
    def __init__(self):
        pyxel.init(160,120,caption="Ball Game")
        self.balls = [Ball(10,10,4,(random.random(),random.random())),Ball(10,10,4,(random.random(),random.random()))]
        self.score = 0
        self.paddle = Paddle(0,0)
        pyxel.run(self.update,self.draw)
    
    #Update everything
    def update(self):
        #Quit game if player presses escape key
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()
        
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
        self.paddle = Paddle(pyxel.mouse_x,pyxel.mouse_y)
    
    #Draw everything
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

App()













