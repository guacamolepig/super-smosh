import os

import pygame as pg

from filetools import list_folders, list_files

class Resources:

    def __init__(self, root):
        self.music_directory = os.path.join(root, 'music')
        self.graphics_directory = os.path.join(root, 'graphics')
        self.sounds_directory = os.path.join(root, 'sounds')

    @property
    def graphics(self):
        g = Resource(self.graphics_directory)
        return self.load_graphics(g)

    @property
    def music(self):
        return Resource(self.music_directory)

    @property
    def sounds(self):
        return Resource(self.sounds_directory)

    def load_graphics(self, graphics):
        for img_name, img_data in graphics._data.items():
            image = pg.image.load(img_data.filepath)
            if image.get_alpha():
                image = image.convert_alpha()
            else:
                image = image.convert()
            setattr(graphics, img_data.name, image)
            graphics._data[img_name] = graphics
        return graphics

class Resource:

    def __init__(self, directory):
        self._directory = directory
        self._set_attributes()

    @property
    def _data(self):
        data = {}
        for filepath in list_files(self._directory):
            d = File(filepath)
            data[d.name] = d
        return data

    def _set_attributes(self):
        for resource in self._data.values():
            setattr(self, resource._name, resource)
class File:

    def __init__(self, filepath):
        self.filepath = filepath

    @property
    def name(self):
        return os.path.splitext(os.path.basename(self.filepath))[0]

    @property
    def ext(self):
        return os.path.splitext(os.path.basename(self.filepath))[1]

    @property
    def _name(self):
        return self.name.replace(' ', '_')
