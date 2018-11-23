# -*- coding: utf-8 -*-


#imports
import pyxel
import utility


#Hub (overworld)
class Hub:
    #Player in Hub with pyx
    class Player():
        def __init__(self,_pyx=0):
            self.pyx=_pyx
    
    
    #Initialize the Player, Hub, and Characters
    def __init__(self):
        #Initialize Player
        self.player = self.Player()
        
        #Initialize Hub
        self.hub = []
        for i in range(0,int(pyxel.width/8)):
            newList = []
            self.hub.append(newList)
            for j in range(0,int(pyxel.height/8)):
                self.hub[i].append(0)
        
        #Initialize Characters and place Player in hub
        self.hub[0][4] = -1
        self.hub[1][1] = utility.Location.TEMPLATE
        self.hub[4][1] = utility.Location.ORBS
        self.hub[7][1] = utility.Location.ASTEROIDS

    
    
    #Update Hub
    def update(self):
        #Find Player
        player_pos=None
        for x in range(0,int(pyxel.width/8)):
            for y in range(0,int(pyxel.height/8)):
                if self.hub[x][y] == -1:
                    player_pos = (x,y)
        #Move Player up one space
        if pyxel.btnp(pyxel.KEY_W,10,3):
            if player_pos[1] != 0 and self.hub[player_pos[0]][player_pos[1]-1] == 0:
                self.hub[player_pos[0]][player_pos[1]]=0
                self.hub[player_pos[0]][player_pos[1]-1]=-1
                player_pos=(player_pos[0],player_pos[1]-1)
        #Move Player left one space
        elif pyxel.btnp(pyxel.KEY_A,10,3):
            if player_pos[0] != 0 and self.hub[player_pos[0]-1][player_pos[1]] == 0:
                self.hub[player_pos[0]][player_pos[1]]=0
                self.hub[player_pos[0]-1][player_pos[1]]=-1
                player_pos=(player_pos[0]-1,player_pos[1])
        #Move Player down one space
        elif pyxel.btnp(pyxel.KEY_S,10,3):
            if player_pos[1] != int(pyxel.height/8)-1 and self.hub[player_pos[0]][player_pos[1]+1] == 0:
                self.hub[player_pos[0]][player_pos[1]]=0
                self.hub[player_pos[0]][player_pos[1]+1]=-1
                player_pos=(player_pos[0],player_pos[1]+1)
        #Move player right one space
        elif pyxel.btnp(pyxel.KEY_D,10,3):
            if player_pos[0] != int(pyxel.width/8)-1 and self.hub[player_pos[0]+1][player_pos[1]] == 0:
                self.hub[player_pos[0]][player_pos[1]]=0
                self.hub[player_pos[0]+1][player_pos[1]]=-1
                player_pos=(player_pos[0]+1,player_pos[1])
        #Activate nearby Game
        elif pyxel.btnp(pyxel.KEY_E):
            #Activate Game one space above Player
            if player_pos[1] != 0 and self.hub[player_pos[0]][player_pos[1]-1] != 0:
                return self.hub[player_pos[0]][player_pos[1]-1]
            #Activate Game one space to the left of Player
            elif player_pos[0] != 0 and self.hub[player_pos[0]-1][player_pos[1]] != 0:
                return self.hub[player_pos[0]-1][player_pos[1]]
            #Activate Game one space below Player
            elif player_pos[1] != int(pyxel.height/8)-1 and self.hub[player_pos[0]][player_pos[1]+1] != 0:
                return self.hub[player_pos[0]][player_pos[1]+1]
            #Activate Game one space to the right of Player
            elif player_pos[0] != int(pyxel.width/8)-1 and self.hub[player_pos[0]+1][player_pos[1]] != 0:
                return self.hub[player_pos[0]+1][player_pos[1]]
        
        return utility.Location.HUB
    
    
    #Draw Hub
    def draw(self):
        #Clear screen
        pyxel.cls(0)
        
        #Write Instructions
        pyxel.text(2,96,"Instructions:",2)
        pyxel.text(2,104,"WASD - Movement",2)
        pyxel.text(2,112,"E    - Execute Nearby Game",2)
        pyxel.text(2,120,"ESC  - Exit RetroHub",2)
        
        #Draw Hub
        for x in range(0,len(self.hub)):
            for y in range(0,len(self.hub[x])):
                #Ignore blank spaces
                if self.hub[x][y] != 0:
                    #Draw Player
                    if self.hub[x][y] == -1:
                        pyxel.blt(x*8, y*8, 0, 0, 8, 8, 8, 0)
                    #Draw Template Icon
                    elif self.hub[x][y] == utility.Location.TEMPLATE:
                        pyxel.blt(x*8, y*8, 0, 0, 16, 8, 8, 0)
                    #Draw Orbs Icon
                    elif self.hub[x][y] == utility.Location.ORBS:
                        pyxel.blt(x*8, y*8, 0, 0, 24, 8, 8, 0)
                    elif self.hub[x][y] == utility.Location.ASTEROIDS:
                        pyxel.blt(x*8, y*8, 0, 0, 32, 8, 8, 0)

