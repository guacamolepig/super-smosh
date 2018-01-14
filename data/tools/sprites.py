import pygame as pg

from ..sprites.player import Player

def load_all_sprites(game):
    all_sprites = pg.sprite.LayeredUpdates()
    platforms = pg.sprite.Group()
    powerups = pg.sprite.Group()
    mobs = pg.sprite.Group()
    clouds = pg.sprite.Group()
    all_sprites.add(Player(game))
    return all_sprites
