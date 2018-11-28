# -*- coding: utf-8 -*-

# IMPORTS
import pyxel
import random
import math

class Asteroids:

    # INDIVIDUAL ASTEROIDS
    class Asteroid:
        def __init__(self):
            # SETS A SPAWN POINT
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

            # GIVES ASTEROIDS A VELOCITY
            self.get_vector(self.spawncorner)

            #GIVES ASTEROIDS A COLOR
            self.color = random.randint(1,15)

            # GIVES ASTEROIDS A RADIUS
            self.radius = 2

        # CALCULATES A VELOCITY
        def get_vector(self, corner):
            if corner == 1:
                self.xvel = float(random.uniform(-0.99, -0.1))
                self.yvel = float(random.uniform(0.1, 0.99))
            if corner == 2:
                self.xvel = float(random.uniform(0.1, 0.99))
                self.yvel = float(random.uniform(0.1, 0.99))
            if corner == 3:
                self.xvel = float(random.uniform(0.1, 0.99))
                self.yvel = float(random.uniform(-0.99, 0.1))
            if corner == 4:
                self.xvel = float(random.uniform(-0.99, -0.1))
                self.yvel = float(random.uniform(-0.99, -0.1))


    # PLAYER
    class Player:
        def __init__(self):
            self.xloc = pyxel.width // 2
            self.yloc = pyxel.height // 2
            self.yvel = 0.4
            self.xvel = 0.4
            self.radius = 2

    # INITIALIZATION FOR GAME CLASS
    def __init__(self):
        self.parts_of_seconds = 0
        self.seconds = 0
        self.minutes = 0
        self.elapsed_seconds = 0
        self.asteroids = []
        self.player = self.Player()
        self.spawn_rate = 1
        self.dist = 0
        self.go_on = True
        self.now_timer = ""
        self.ch_upg = False
        self.upgrade_velocity = False
        self.upgrade_teleportation = False
        self.upgrade_clear = False
        self.upgrade_shield = False
        self.used_nuke = 0

    # UPDATE THE GAME'S LOGIC
    def update(self):
        # RETURN TO HUB IF 'B' IS PRESSED
        if pyxel.btnp(pyxel.KEY_B):
            return True

        # LETS USER CHOOSE AN UPGRADE
        if not self.ch_upg:
            pyxel.mouse(True)
            if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
                if 21 <= pyxel.mouse_y <= (pyxel.height / 2) + 5 and 21 <= pyxel.mouse_x <= (pyxel.width / 2) - 5:
                    self.upgrade_velocity = True
                    self.ch_upg = True
                if 21 <= pyxel.mouse_y <= (pyxel.height / 2) + 5 and (pyxel.width / 2) + 5 <= pyxel.mouse_x <= pyxel.width - 21:
                    self.upgrade_teleportation = True
                    self.ch_upg = True
                if (pyxel.height / 2) + 5 <= pyxel.mouse_y <= pyxel.height - 21 and 21 <= pyxel.mouse_x <= (pyxel.width / 2) - 5:
                    self.upgrade_clear = True
                    self.ch_upg = True
                if (pyxel.height / 2) + 5 <= pyxel.mouse_y <= pyxel.height - 21 and (pyxel.width / 2) + 5 <= pyxel.mouse_x <= pyxel.width - 21:
                    self.upgrade_shield = True
                    self.ch_upg = True
        else:
            # CHECKS IF THE GAME IS ENDED
            if self.go_on:

                # APPLIES VELOCITY UPGRADE
                if self.upgrade_velocity:
                    self.player.yvel = 1.0
                    self.player.xvel = 1.0


                # APPLIES THE TELEPORTATION UPGRADE
                if self.upgrade_teleportation:
                    if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
                        self.player.xloc = pyxel.mouse_x
                        self.player.yloc = pyxel.mouse_y

                # GETS THE CURRENT GAME TIME
                self.now_timer = self.timer()

                # ASTEROID LOGIC
                for asteroid in self.asteroids:

                    # CHANGES POSITION BASED ON VELOCITY
                    asteroid.x += asteroid.xvel
                    asteroid.y += asteroid.yvel

                    # REMOVES ASTEROID IF OUT OF FRAME
                    if asteroid.x > pyxel.width + 4 or asteroid.x < -4:
                        self.asteroids.remove(asteroid)
                        continue
                    if asteroid.y > pyxel.height + 4 or asteroid.y < -4:
                        self.asteroids.remove(asteroid)

                    # CHECKS IF ASTEROID IS OVERLAPPING WITH PLAYER ENTITY
                    self.dist = math.sqrt(math.pow((asteroid.x - self.player.xloc), 2) +
                                          math.pow((asteroid.y - self.player.yloc), 2))
                    if self.dist < self.player.radius + asteroid.radius:
                        self.go_on = False


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

                # CALCULATES SPAWN RATE
                if pyxel.frame_count % 120 == 0:
                    self.spawn_rate += 1

                # ADDS ASTEROIDS BY SPAWN RATE
                if pyxel.frame_count % int((90/self.spawn_rate)) == 0:
                    self.asteroids.append(self.Asteroid())

                # APPLIES THE NUKE UPGRADE
                if self.upgrade_clear:
                    if pyxel.btnp(pyxel.KEY_E) and self.used_nuke != 3:
                        self.used_nuke += 1
                        self.asteroids = []


        # KEEPS THE GAME GOING
        return False

    # CALCULATES THE CURRENT IN GAME TIME
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

    # DRAWS THE GAME
    def draw(self):
        # DRAWS UPGRADE BUTTONS
        if not self.ch_upg:
            pyxel.cls(0)
            pyxel.rect(20, 20, (pyxel.width / 2) - 5, (pyxel.height / 2) - 5, 5)
            pyxel.text(29,21,"Extra Velocity",15)
            pyxel.text(21,30,"Increases Velocity",15)
            pyxel.rect((pyxel.width / 2) + 5, 20, pyxel.width - 21, (pyxel.height / 2) - 5, 9)
            pyxel.text((pyxel.width / 2) + 15, 21,"Teleportation", 15)
            pyxel.text((pyxel.width / 2) + 19, 30,"Left Click", 15)
            pyxel.rect(20, (pyxel.height / 2) + 5, (pyxel.width / 2) - 5, pyxel.height - 21, 7)
            pyxel.text(33, (pyxel.height / 2) + 6,"Nuke the Map", 15)
            pyxel.text(33, (pyxel.height / 2) + 15,"3 Time Limit", 15)
            pyxel.text(38, (pyxel.height / 2) + 24,"Press 'E'", 15)
            pyxel.rect((pyxel.width / 2) + 5, (pyxel.height / 2) + 5, pyxel.width - 21, pyxel.height - 21, 8)
            pyxel.text((pyxel.width / 2) + 25, (pyxel.height / 2) + 6,"WIP", 15)
            pyxel.text(64, 10, "Choose an Upgrade", 15)

        else:
            # CHECKS IF THE GAME IS ONGOING
            if self.go_on:

                # HIDES THE CURSOR
                if not self.upgrade_teleportation:
                    pyxel.mouse(False)

                # CLEARS THE SCREEN
                pyxel.cls(0)

                # DISPLAYS THE TIMER
                pyxel.text(2, 2, str(self.now_timer), 10)

                # DRAWS EACH ASTEROID AT X, Y
                for asteroid in self.asteroids:
                    pyxel.circ(asteroid.x, asteroid.y, asteroid.radius, asteroid.color)

                # DRAWS THE PLAYER AT X, Y
                pyxel.circ(self.player.xloc, self.player.yloc, self.player.radius, 3)

            # IF GAME IS DONE
            else:
                pyxel.cls(0)
                pyxel.text(60,50,f"You lasted: {self.now_timer}", 10)
                pyxel.text(45, 70, "Press the 'B' key to return", 10)
