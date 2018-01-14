import pygame as pg

from .tools import engine
from .settings import *

""" initialise the pygame """

pg.init()
pg.display.set_caption(GAME_CAPTION)
pg.display.set_mode(SCREEN_SIZE)

def run(root):
    game = engine.Engine(root)
    game.setup()
    game.mainloop()
