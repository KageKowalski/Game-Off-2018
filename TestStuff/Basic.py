# -*- coding: utf-8 -*-

import pyxel

pyxel.init(160, 120)

def update():
    if pyxel.btnp(pyxel.KEY_ESCAPE):
        pyxel.quit()

def draw():
    pyxel.cls(0)
    pyxel.rect(15, 10, 20, 20, 15)

pyxel.run(update, draw)