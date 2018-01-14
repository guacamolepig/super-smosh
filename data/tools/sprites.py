import pygame as pg

from ..sprites.player import Player

def load_all_sprites(game):
    all_sprites = pg.sprite.Group()
    all_sprites.add(load_player(game))
    return all_sprites

def load_player(game):
    return Player(game)
