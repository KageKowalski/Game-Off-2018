# -*- coding: utf-8 -*-


#imports
import pyxel
import random
import math


#Orbs game
class Orbs:
    #Ball entity
    class Ball:
        def __init__(self,_v,_x=float(192/2),_y=float(128/2),_r=4,_c=random.randint(1,15)):
            self.x = _x
            self.y = _y
            self.r = _r
            self.v = _v
            self.c = _c
            self.invincibility_counter = 0
    
    
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
    
    
    #Initialize data
    def __init__(self):
        self.balls = [self.Ball(((random.random()+0.5)/3,(random.random()+0.5)/3))]
        self.score = 0
        self.paddle = self.Paddle(0,0)
        self.game_over = False
    
    
    #Update Orbs
    def update(self):
        #Update game over menu
        if self.game_over:
            #Return to hub if player presses 'B' key
            if pyxel.btnp(pyxel.KEY_B):
                return True
        
        #Update game
        else:
            #End game if player presses 'B' key
            if pyxel.btnp(pyxel.KEY_B):
                self.game_over=True
            
            #Move paddle
            self.paddle = self.Paddle(pyxel.mouse_x,pyxel.mouse_y)
            
            #Handle collisions
            for ball in self.balls:
                #Move balls
                ball.x = ball.x + ball.v[0]
                ball.y = ball.y + ball.v[1]
                
                #Handle ball-window collisions
                if ball.x + ball.r >= pyxel.width or ball.x - ball.r <= 0:
                    self.game_over = True
                elif ball.y + ball.r >= pyxel.height or ball.y - ball.r <= 0:
                    self.game_over = True
                    
                #Handle ball-paddle collisions
                elif math.sqrt( ((ball.x-self.paddle.ulc[0])**2)+((ball.y-self.paddle.ulc[1])**2) ) <= ball.r or math.sqrt( ((ball.x-self.paddle.urc[0])**2)+((ball.y-self.paddle.urc[1])**2) ) <= ball.r or math.sqrt( ((ball.x-self.paddle.llc[0])**2)+((ball.y-self.paddle.llc[1])**2) ) <= ball.r or math.sqrt( ((ball.x-self.paddle.lrc[0])**2)+((ball.y-self.paddle.lrc[1])**2) ) <= ball.r:
                    if pyxel.frame_count - ball.invincibility_counter > 10:
                        ball.v = (((random.random()-0.5)/3)-ball.v[0],((random.random()-0.5)/3)-ball.v[1])
                        self.score = self.score + 1
                        
                        #Move ball out of paddle
                        while math.sqrt( ((ball.x-self.paddle.ulc[0])**2)+((ball.y-self.paddle.ulc[1])**2) ) <= ball.r or math.sqrt( ((ball.x-self.paddle.urc[0])**2)+((ball.y-self.paddle.urc[1])**2) ) <= ball.r or math.sqrt( ((ball.x-self.paddle.llc[0])**2)+((ball.y-self.paddle.llc[1])**2) ) <= ball.r or math.sqrt( ((ball.x-self.paddle.lrc[0])**2)+((ball.y-self.paddle.lrc[1])**2) ) <= ball.r:
                            ball.x = ball.x + ball.v[0]
                            ball.y = ball.y + ball.v[1]
                        for i in range (0,5):
                            ball.x = ball.x + ball.v[0]
                            ball.y = ball.y + ball.v[1]
                        
                        #Add new ball to game
                        if self.score%25==0:
                            self.balls.append(self.Ball(((random.random()+0.5)/3,(random.random()+0.5)/3)))
                        
                        ball.invincibility_counter=pyxel.frame_count
        
        return False
    
    
    #Draw Orbs
    def draw(self):
        #Clear screen
        pyxel.cls(0)
        
        #Draw game over graphics
        if self.game_over:
            #Draw game over and score text
            pyxel.text(8,8,"GAME OVER",2)
            pyxel.text(8,16,"Score: " + str(self.score),2)
        
        #Draw game graphics
        else:
            #Draw paddle
            pyxel.rect(self.paddle.x-self.paddle.hl,self.paddle.y-self.paddle.hl,self.paddle.x+self.paddle.hl,self.paddle.y+self.paddle.hl,self.paddle.c)
            
            #Draw balls
            for ball in self.balls:
                pyxel.circ(ball.x,ball.y,ball.r,ball.c)
            
            #Draw score
            pyxel.text(2,2,str(self.score),random.randint(1,15))
    
        
    #Get pyx
    def getPyx(self):
        #Replace "None" with the amount of pyx player wins upon game over
        return int(self.score/10)

