# -*- coding: utf-8 -*-

import pyxel

class App:
    def __init__(self):
        pyxel.init(160, 120, caption="Look at my Square!")
        self.x = 0
        self.y = 0
        pyxel.run(self.update, self.draw)
        
    def update(self):
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()
        
        self.x = (self.x + 1) % (160 - 7)
        
        if self.x == 0:
            self.y = (self.y + 7) % (120 - 7)
        
    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.x, self.y, self.x + 7, self.y + 7, 10)

App()