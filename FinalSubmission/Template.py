# -*- coding: utf-8 -*-


#imports
import pyxel


#TEMPLATE game
class Template:
    #Initialize the game
    def __init__(self):
        None #CODE TO INITILIZE GAME GOES HERE (DELETE NONE)
    
    
    #Update the game
    def update(self):
        #Return to Hub if Player presses 'B' key
        if pyxel.btnp(pyxel.KEY_B):
            return True
        
        #CODE TO UPDATE GAME GOES HERE
        
        return False
    
    
    #Draw the game
    def draw(self):
        #Clear screen
        pyxel.cls(0)
        
        #CODE TO DRAW GAME GOES HERE
    
    
    #Get pyx
    def getPyx(self):
        #Replace 0 with the amount of pyx player wins upon game over
        #Conversion rate guidelines:
        #Win 0 ~ 5 pyx: player did poorly
        #Win 5 ~ 10 pyx: player did fine
        #Win > 10 pyx: player did well
        return 0

