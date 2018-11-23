# -*- coding: utf-8 -*-
import pyxel
import random

class Asteroids:

    class Asteroid:
        def __init__(self):
            self.spawncorner = random.randint(1,4)
            if self.spawncorner == 1:
                self.x= pyxel.width - 2
                self.y= 2
            elif self.spawncorner == 2:
                self.x= 2
                self.y= 2
            elif self.spawncorner == 3:
                self.x= 2
                self.y = pyxel.height - 2
            elif self.spawncorner == 4:
                self.x= pyxel.width - 2
                self.y= pyxel.height - 2
            self.get_vector(self.spawncorner)
            self.color = random.randint(1,15)
            self.radius = 2

        def get_vector(self, corner):
            if corner == 1:
                self.xvel = float(random.uniform(-0.99, -0.01))
                self.yvel = float(random.uniform(0.01, 0.99))
            if corner == 2:
                self.xvel = float(random.uniform(0.01, 0.99))
                self.yvel = float(random.uniform(0.01, 0.99))
            if corner == 3:
                self.xvel = float(random.uniform(0.01, 0.99))
                self.yvel = float(random.uniform(-0.99, 0.01))
            if corner == 4:
                self.xvel = float(random.uniform(-0.99, -0.1))
                self.yvel = float(random.uniform(-0.99, -0.1))

    class Player:
        def __init__(self):
            self.xloc = pyxel.width // 2
            self.yloc = pyxel.height // 2
            self.yvel = 0.4
            self.xvel = 0.4


    def __init__(self):
        self.parts_of_seconds = 0
        self.seconds = 0
        self.minutes = 0
        self.elapsed_seconds = 0
        self.asteroids = []
        self.player = self.Player()
        self.spawn_rate = 1

    #Update the game
    def update(self):
        #Return to Hub if Player presses 'B' key
        if pyxel.btnp(pyxel.KEY_B):
            return True

        for asteroid in self.asteroids:
            asteroid.x += asteroid.xvel
            asteroid.y += asteroid.yvel
            if asteroid.x > pyxel.width + 4 or asteroid.x < -4:
                self.asteroids.remove(asteroid)
                continue
            if asteroid.y > pyxel.height + 4 or asteroid.y < -4:
                self.asteroids.remove(asteroid)

        # MOVEMENT
        if pyxel.btn(pyxel.KEY_W) and pyxel.btn(pyxel.KEY_D):
            self.player.yloc -= self.player.yvel
            self.player.xloc += self.player.xvel
        elif pyxel.btn(pyxel.KEY_W) and pyxel.btn(pyxel.KEY_A):
            self.player.yloc -= self.player.yvel
            self.player.xloc -= self.player.xvel
        elif pyxel.btn(pyxel.KEY_S) and pyxel.btn(pyxel.KEY_A):
            self.player.yloc += self.player.yvel
            self.player.xloc -= self.player.xvel
        elif pyxel.btn(pyxel.KEY_S) and pyxel.btn(pyxel.KEY_D):
            self.player.yloc += self.player.yvel
            self.player.xloc += self.player.xvel
        elif pyxel.btn(pyxel.KEY_W):
            self.player.yloc -= self.player.yvel
        elif pyxel.btn(pyxel.KEY_A):
            self.player.xloc -= self.player.xvel
        elif pyxel.btn(pyxel.KEY_S):
            self.player.yloc += self.player.yvel
        elif pyxel.btn(pyxel.KEY_D):
            self.player.xloc += self.player.xvel

        if pyxel.frame_count % 120 == 0:
            self.spawn_rate += 1

        if pyxel.frame_count % int((90/self.spawn_rate)) == 0:
            self.asteroids.append(self.Asteroid())


        return False
    
    def timer(self):
        self.parts_of_seconds += 1
        if self.parts_of_seconds == 30:
            self.parts_of_seconds = 0
            self.seconds += 1
            self.elapsed_seconds += 1
            if self.seconds % 60 == 0:
                self.seconds = 0
                self.minutes += 1
        if self.minutes < 10:
            if self.seconds < 10:
                return f"0{self.minutes}:0{self.seconds}"
            else:
                return f"0{self.minutes}:{self.seconds}"
        else:
            if self.seconds < 10:
                return f"{self.minutes}:0{self.seconds}"
            else:
                return f"{self.minutes}:{self.seconds}"

    #Draw the game
    def draw(self):
        #Clear screen
        pyxel.cls(0)
        pyxel.text(2, 2, str(self.timer()), 10)
        for asteroid in self.asteroids:
            pyxel.circ(asteroid.x, asteroid.y, asteroid.radius, asteroid.color)
        pyxel.circ(self.player.xloc, self.player.yloc, 2, 3)

