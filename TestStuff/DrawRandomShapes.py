# -*- coding: utf-8 -*-

import pyxel
import random

#Class representing a square
class Square:
    def __init__(self, _x0, _y0):
        self.x1 = _x0
        self.y1 = _y0
        self.x2 = _x0
        self.y2 = _y0
        self.t = "square"
        self.c = random.randint(1,15)

#Class representing a circle
class Circle:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y
        self.r = 1
        self.t = "circle"
        self.c = random.randint(1,15)
        

class App:
    def __init__(self):
        pyxel.init(160,120,caption="Draw Random Shapes")
        pyxel.mouse(True)
        self.shapes = []
        pyxel.run(self.update,self.draw)
    
    def update(self):
        #Quit Game on Escape
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()
        
        #Create Shape on Left Click
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            if random.random() > 0.5:
                self.shapes.append(Square(pyxel.mouse_x, pyxel.mouse_y))
            else:
                self.shapes.append(Circle(pyxel.mouse_x, pyxel.mouse_y))
    
    def draw(self):
        pyxel.cls(0)
        
        #Handle Shapes
        for shape in self.shapes:
            if shape.t == "square":
                if shape.x1 >= 0 and shape.y1 >= 0 and shape.x2 <= pyxel.width and shape.y2 <= pyxel.height:
                    pyxel.rectb(shape.x1, shape.y1, shape.x2, shape.y2, shape.c)
                    shape.x1 = shape.x1 - 1
                    shape.y1 = shape.y1 - 1
                    shape.x2 = shape.x2 + 1
                    shape.y2 = shape.y2 + 1
                else:
                    self.shapes.remove(shape)
            elif shape.t == "circle":
                if shape.x + shape.r <= pyxel.width and shape.x - shape.r >= 0 and shape.y + shape.r <= pyxel.height and shape.y - shape.r >= 0:
                    pyxel.circb(shape.x, shape.y, shape.r, shape.c)
                    shape.r = shape.r + 1
                else:
                    self.shapes.remove(shape)

App()




















