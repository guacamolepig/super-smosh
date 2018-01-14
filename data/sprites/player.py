import pygame as pg
from ..settings import *
vec = pg.math.Vector2


class Player(pg.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
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

        self.acc_rate = 1
        self.vel_friction = -0.1

    def update(self):
        self.animate()
        self.calculate()

    def calculate(self):
        keys = pg.key.get_pressed()

        self.acc = vec(0, 0)
        if keys[pg.K_RIGHT]:
            self.acc.x = self.acc_rate
        if keys[pg.K_LEFT]:
            self.acc.x = -self.acc_rate

        self.acc.x += self.vel.x * self.vel_friction
        print(self.acc.x)
        self.vel += self.acc
        if abs(self.vel.x) < 0.1:
            self.vel.x = 0
        self.pos += self.vel + 0.5 * self.acc
        if self.pos.x > SCREEN_SIZE[0] + self.rect.width / 2:
            self.pos.x = 0 - self.rect.width / 2
        if self.pos.x < 0 - self.rect.width / 2:
            self.pos.x = SCREEN_SIZE[1] + self.rect.width / 2
        self.rect.midbottom = self.pos

    def animate(self):
        self.now = pg.time.get_ticks()
        self.mask = pg.mask.from_surface(self.image)
