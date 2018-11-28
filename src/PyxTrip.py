# -*- coding: utf-8 -*-


#imports
import pyxel
import enum


#TEMPLATE game
class PyxTrip:
    class Entity(enum.Enum):
        BLANK=0
        PLAYER=-1
        BLOCK=1
    
    
    #Initialize the game
    def __init__(self):
        #Initialize variables
        self.GRID_WIDTH=int(pyxel.width/8)
        self.GRID_HEIGHT=3
        self.grid=[]
        
        #Fill grid
        for i in range(self.GRID_WIDTH):
            self.grid.append([])
            for j in range(self.GRID_HEIGHT):
                self.grid[i].append(self.Entity.BLANK)
        self.grid[int(self.GRID_WIDTH/3)][0]=self.Entity.PLAYER
        self.grid[int(self.GRID_WIDTH/3)][1]=self.Entity.PLAYER
    
    
    #Update the game
    def update(self):
        #Return to Hub if Player presses 'B' key
        if pyxel.btnp(pyxel.KEY_B):
            return True
        
        
        
        return False
    
    
    #Draw the game
    def draw(self):
        #Clear screen
        pyxel.cls(0)
        
        #CODE TO DRAW GAME GOES HERE
    
    
    #Get pyx
    def getPyx(self):
        return 0

