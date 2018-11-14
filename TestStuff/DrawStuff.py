# -*- coding: utf-8 -*-

import pyxel

class App:
    def __init__(self):
        pyxel.init(160,120,caption="DrawStuff")
        pyxel.image(0).load(0,0,"assets/DrawStuffImage.png")
        pyxel.run(self.update, self.draw)
    
    def update(self):
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()
    
    def draw(self):
        pyxel.cls(0)
        pyxel.text(80,30,"!BeeP BeeP!",pyxel.frame_count%16)
        pyxel.blt(0,0,0,0,0,80,60)

App()