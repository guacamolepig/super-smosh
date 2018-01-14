import os

import pygame as pg

from ..settings import *
from ..tools import resources as rsc
from ..tools import sprites

class Engine:

    def __init__(self, root):
        self.done = False
        self.fps = SCREEN_FPS
        self.root = root
        self.resources_directory = os.path.join(self.root, 'resources')

    def setup(self):
        self.clock = pg.time.Clock()
        self.screen = pg.display.get_surface()
        self.rsc = rsc.Resources(self.resources_directory)
        self.all_sprites = sprites.load_all_sprites(self)
        pg.mixer.music.load(self.rsc.music.Intro.filepath)
        # pg.mixer.music.play(-1)

    def mainloop(self):
        while not self.done:
            self.clock.tick(self.fps)
            self.event_handler()
            self.update()
            self.draw()

    def event_handler(self):
        self.events = pg.event.get()
        for event in self.events:
            if event.type == pg.QUIT:
                self.done = True

    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.screen.fill((0,0,0))
        self.all_sprites.draw(self.screen)
        pg.display.flip()
