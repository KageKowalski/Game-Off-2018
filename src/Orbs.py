# -*- coding: utf-8 -*-


#imports
import pyxel
import random
import math
import utility


#Orbs game
class Orbs:
    #Ball entity
    class Ball:
        def __init__(self,_v,_x=float(192/2),_y=float(128/2)):
            self.x = _x
            self.y = _y
            self.r = 4
            self.v = _v
            self.invincibility_counter = 0
            
            #Change ball color based on velocity
            if abs(self.v[0])+abs(self.v[1]) < 0.7:
                self.c=0
            elif abs(self.v[0])+abs(self.v[1]) < 1.3:
                self.c=1
            else:
                self.c=2
    
    
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
        self.balls = [self.Ball(((random.random()-0.5),(random.random()-0.5)))]
        self.score = 0
        self.paddle = self.Paddle(0,0)
        self.game_state = utility.GameState.GAME_START
    
    
    #Update Orbs
    def update(self):
        #Update game
        if self.game_state==utility.GameState.IN_PROGRESS:            
            #Move paddle
            self.paddle = self.Paddle(pyxel.mouse_x,pyxel.mouse_y)
            
            #Handle collisions
            for ball in self.balls:
                #Move balls
                ball.x = ball.x + ball.v[0]
                ball.y = ball.y + ball.v[1]
                
                #Handle ball-window collisions
                if ball.x + ball.r >= pyxel.width or ball.x - ball.r <= 0:
                    self.game_state = utility.GameState.GAME_OVER
                elif ball.y + ball.r >= pyxel.height or ball.y - ball.r <= 0:
                    self.game_state = utility.GameState.GAME_OVER
                    
                #Handle ball-paddle collisions
                elif math.sqrt( ((ball.x-self.paddle.ulc[0])**2)+((ball.y-self.paddle.ulc[1])**2) ) <= ball.r or math.sqrt( ((ball.x-self.paddle.urc[0])**2)+((ball.y-self.paddle.urc[1])**2) ) <= ball.r or math.sqrt( ((ball.x-self.paddle.llc[0])**2)+((ball.y-self.paddle.llc[1])**2) ) <= ball.r or math.sqrt( ((ball.x-self.paddle.lrc[0])**2)+((ball.y-self.paddle.lrc[1])**2) ) <= ball.r:
                    if pyxel.frame_count - ball.invincibility_counter > 10:
                        ball.v = (((random.random()-0.5)/3)-ball.v[0],((random.random()-0.5)/3)-ball.v[1])
                        self.score = self.score + 1
                        
                        #Change ball color based on velocity
                        if abs(ball.v[0])+abs(ball.v[1]) < 0.7:
                            ball.c=0
                        elif abs(ball.v[0])+abs(ball.v[1]) < 1.3:
                            ball.c=1
                        else:
                            ball.c=2
                        
                        #Move ball out of paddle
                        while math.sqrt( ((ball.x-self.paddle.ulc[0])**2)+((ball.y-self.paddle.ulc[1])**2) ) <= ball.r or math.sqrt( ((ball.x-self.paddle.urc[0])**2)+((ball.y-self.paddle.urc[1])**2) ) <= ball.r or math.sqrt( ((ball.x-self.paddle.llc[0])**2)+((ball.y-self.paddle.llc[1])**2) ) <= ball.r or math.sqrt( ((ball.x-self.paddle.lrc[0])**2)+((ball.y-self.paddle.lrc[1])**2) ) <= ball.r:
                            ball.x = ball.x + ball.v[0]
                            ball.y = ball.y + ball.v[1]
                        for i in range (0,5):
                            ball.x = ball.x + ball.v[0]
                            ball.y = ball.y + ball.v[1]
                        
                        #Add new ball to game
                        if self.score%25==0:
                            self.balls.append(self.Ball(((random.random()-0.5),(random.random()-0.5))))
                        
                        ball.invincibility_counter=pyxel.frame_count
        
        #Update game start menu
        elif self.game_state==utility.GameState.GAME_START:
            #Move game state to in progress if player presses 'E' key
            if pyxel.btnp(pyxel.KEY_E):
                self.game_state=utility.GameState.IN_PROGRESS
        
        #Update game over menu
        elif self.game_state==utility.GameState.GAME_OVER:
            #Return to hub if player presses 'B' key
            if pyxel.btnp(pyxel.KEY_B):
                return True
        
        else:
            print("Error: Impossible Game State")
        
        return False
    
    
    #Draw Orbs
    def draw(self):
        #Clear screen
        pyxel.cls(0)
        
        #Draw game
        if self.game_state==utility.GameState.IN_PROGRESS:
            #Draw paddle
            pyxel.blt(self.paddle.ulc[0],self.paddle.ulc[1],0,56,8,8,8,0)
            
            #Draw balls
            for ball in self.balls:
                if ball.c==0:
                    pyxel.blt(ball.x-3,ball.y-3,0,32,8,8,8,0)
                elif ball.c==1:
                    pyxel.blt(ball.x-3,ball.y-3,0,40,8,8,8,0)
                elif ball.c==2:
                    pyxel.blt(ball.x-3,ball.y-3,0,48,8,8,8,0)
                else:
                    print("ERROR: Impossible Orb Color")
            
            #Draw score
            pyxel.text(2,2,str(self.score),random.randint(1,15))
        
        #Draw game start menu
        elif self.game_state==utility.GameState.GAME_START:
            #Draw instructions
            pyxel.text(8,8,"Welcome to Orbs!",2)
            pyxel.text(8,24,"Stop orbs from leaving the screen.",2)
            pyxel.text(8,32,"Deflect orbs with your paddle (mouse).",2)
            pyxel.text(8,48,"Press 'E' to continue.",2)
        
        #Draw game over menu
        elif self.game_state==utility.GameState.GAME_OVER:
            #Draw game over and score text
            pyxel.text(8,8,"GAME OVER",2)
            pyxel.text(8,16,"Score: " + str(self.score),2)
            pyxel.text(8,32,"Press 'B' to return to Hub.",2)
    
    
    #Get pyx
    def getPyx(self):
        #Replace "None" with the amount of pyx player wins upon game over
        return int(self.score/10)

