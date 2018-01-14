import pygame as pg
from ..settings import *
from ..sprites import player_tools as pt
vec = pg.math.Vector2


class Player(pg.sprite.Sprite):
    def __init__(self, game):

        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.walking = False
        self.jumping = False
        self.current_frame = 0
        self.last_update = 0
        self.image = pg.Surface((100, 100))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.midbottom = (SCREEN_SIZE[0]/2, SCREEN_SIZE[1]/2)
        self.pos = vec(SCREEN_SIZE[0]/2, SCREEN_SIZE[1]/2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

        self.acc_rate = 2
        self.vel_friction = -0.1

    def update(self):
        self.animate()
        self.calculate_position()

    def calculate_position(self):
        keys = pg.key.get_pressed()

        self.acc.x = pt.update_accx(self, keys)
        self.acc.y = pt.update_accy(self, keys)

        self.vel.x = pt.update_velx(self)
        self.vel.y = pt.update_vely(self)

        self.pos += self.vel + 0.5 * self.acc

        self.rect.midbottom = self.pos

    def animate(self):
        self.now = pg.time.get_ticks()
        self.mask = pg.mask.from_surface(self.image)
