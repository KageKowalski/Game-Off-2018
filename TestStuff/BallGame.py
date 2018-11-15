# -*- coding: utf-8 -*-

import pyxel
import random
import math

#Balls which bounce around
class Ball:
    def __init__(self,_x=float(80),_y=float(60),_r=4,_v=(random.random(),random.random()),_c=random.randint(1,15)):
        self.x = _x
        self.y = _y
        self.r = _r
        self.v = _v
        self.c = _c

#Paddle which reflects balls
class Paddle:
    def __init__(self,_x,_y,_hl=2,_c=random.randint(1,15)):
        self.x = _x
        self.y = _y
        self.hl = _hl
        self.c = _c

#Application
class App:
    def __init__(self):
        pyxel.init(160,120,caption="Ball Game")
        self.balls = [Ball()]
        pyxel.run(self.update,self.draw)
    
    #Update everything
    def update(self):
        #Quit game if player presses escape key
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()
        
        #Move paddle
        self.paddle = Paddle(pyxel.mouse_x,pyxel.mouse_y)
        
        #Move balls
        for ball in self.balls:
            
            self.ulc = (self.paddle.x-self.paddle.hl,self.paddle.y-self.paddle.hl)
            self.urc = (self.paddle.x+self.paddle.hl,self.paddle.y-self.paddle.hl)
            self.llc = (self.paddle.x-self.paddle.hl,self.paddle.y+self.paddle.hl)
            self.lrc = (self.paddle.x+self.paddle.hl,self.paddle.y+self.paddle.hl)
            
            #Handle screen collisions
            if ball.x + ball.r >= 160 or ball.x - ball.r <= 0:
                ball.v = (-ball.v[0],ball.v[1])
            elif ball.y + ball.r >= 120 or ball.y - ball.r <= 0:
                ball.v = (ball.v[0],-ball.v[1])
            #Handle paddle collisions
            elif math.sqrt( ((ball.x-self.ulc[0])**2)+((ball.y-self.ulc[1])**2) ) <= ball.r or math.sqrt( ((ball.x-self.urc[0])**2)+((ball.y-self.urc[1])**2) ) <= ball.r or math.sqrt( ((ball.x-self.llc[0])**2)+((ball.y-self.llc[1])**2) ) <= ball.r or math.sqrt( ((ball.x-self.lrc[0])**2)+((ball.y-self.lrc[1])**2) ) <= ball.r:
                ball.v = (-ball.v[0],-ball.v[1])
            #Handle standard movement
            ball.x = ball.x + ball.v[0]
            ball.y = ball.y + ball.v[1]
    
    #Draw everything
    def draw(self):
        #Clear screen
        pyxel.cls(0)
        
        #Draw paddle
        pyxel.rect(self.paddle.x-self.paddle.hl,self.paddle.y-self.paddle.hl,self.paddle.x+self.paddle.hl,self.paddle.y+self.paddle.hl,self.paddle.c)
        
        #Draw balls
        for ball in self.balls:
            pyxel.circ(ball.x,ball.y,ball.r,ball.c)

App()













