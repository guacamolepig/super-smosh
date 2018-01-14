import pygame as pg
from ..settings import *
vec = pg.math.Vector2

def update_accx(player, keys):
    player.acc.x = 0
    if keys[player.K_RIGHT]:
        player.acc.x = player.acc_rate
    if keys[player.K_LEFT]:
        player.acc.x = -player.acc_rate
    player.acc.x += player.vel.x * player.vel_friction
    return player.acc.x

def update_velx(player):
    player.vel.x += player.acc.x
    if abs(player.vel.x) < 0.1:
        player.vel.x = 0
    return player.vel.x

def update_accy(player, keys):
    player.acc.y = 0
    if keys[player.K_DOWN]:
        player.acc.y = player.acc_rate
    if keys[player.K_UP]:
        player.acc.y = -player.acc_rate
    player.acc.y += player.vel.y * player.vel_friction
    return player.acc.y

def update_vely(player):
    player.vel.y += player.acc.y
    if abs(player.vel.y) < 0.1:
        player.vel.y = 0
    return player.vel.y
