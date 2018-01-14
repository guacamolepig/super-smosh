import pygame as pg
from ..settings import *
from ..sprites import player_tools as pt
vec = pg.math.Vector2


class Player(pg.sprite.Sprite):
    def __init__(self, game, player_number):

        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.player_number = player_number
        self.walking = False
        self.jumping = False
        self.current_frame = 0
        self.last_update = 0
        self.assign_player_features()
        # self.image = pg.Surface((100, 100))
        # self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.midbottom = (SCREEN_SIZE[0]/2, SCREEN_SIZE[1]/2)
        self.pos = vec(SCREEN_SIZE[0]/2, SCREEN_SIZE[1]/2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

        self.acc_rate = 2
        self.vel_friction = -0.1

    def assign_player_features(self):
        if self.player_number == 0:
            self.image = self.game.rsc.graphics.player1
            self.K_LEFT = pg.K_LEFT
            self.K_RIGHT = pg.K_RIGHT
            self.K_UP = pg.K_UP
            self.K_DOWN = pg.K_DOWN
        elif self.player_number == 1:
            self.image = self.game.rsc.graphics.player2
            self.K_LEFT = pg.K_a
            self.K_RIGHT = pg.K_d
            self.K_UP = pg.K_w
            self.K_DOWN = pg.K_s


    def set_keys(self):
        if self.player_number == 0:
            return self.game.rsc.graphics.player1
        elif self.player_number == 1:
            return self.game.rsc.graphics.player2
        else:
            return None

    def update(self):
        self.animate()
        self.calculate_position()

    def calculate_position(self):
        keys = pg.key.get_pressed()

        self.acc.x = pt.update_accx(self, keys)
        self.acc.y = pt.update_accy(self, keys)

        self.vel.x = pt.update_velx(self)
        self.vel.y = pt.update_vely(self)

        self.pos.x = pt.update_posx(self)
        self.pos.y = pt.update_posy(self)


        self.rect.midbottom = self.pos

    def animate(self):
        self.now = pg.time.get_ticks()
        self.mask = pg.mask.from_surface(self.image)
