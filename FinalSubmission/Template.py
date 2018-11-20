# -*- coding: utf-8 -*-


#imports
import pyxel


#TEMPLATE game
class Template:
    #Initialize the game
    def __init__(self):
        None
    
    
    #Update the game
    def update(self):
        #Return to Hub if Player presses 'B' key
        if pyxel.btnp(pyxel.KEY_B):
            return True
    
    
    #Draw the game
    def draw(self):
        None
