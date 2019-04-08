import scipy as sp
import numpy.random as npr

from Entity import Entity
from Terrain import Terrain


class Cell():
    """A single cell of a field.

    It contains entities and/or attributes for a single cell (i.e. how much
    food is in the cell)
    """

    total_cells = 0

    def __init__(self, i, j, field):
        Cell.total_cells += 1
        self.__cell_n = Cell.total_cells
        self._is_empty = True
        self.__entity = None
        self.__terrain = Terrain(field, self)
        self.__coordinates = (i, j)
        self.field = field

    def __repr__(self):
        i, j = self.__coordinates
        s = 'Cell number {} of {}\n'.format(self.__cell_n, Cell.total_cells)
        s += 'Cell is currently '
        if self._is_empty:
            s += 'empty\n'
        else:
            s += 'not empty\n'
        s += "The Cell's coordinates are ({} {})".format(i, j)
        return s

    def __str__(self):
        return self.__repr__()

    @property
    def entity(self):
        return self.__entity

    @entity.setter
    def entity(self, obj):
        self.__entity = obj

    @entity.deleter
    def entity(self):
        del self.__entity

    @property
    def terrain(self):
        """Terrain info a dictionary?"""
        return self.__terrain

    @terrain.setter
    def terrain(self, terrain_info):
        self.__terrain = terrain_info

    @terrain.deleter
    def terrain(self):
        del self.__terrain

    @property
    def coordinates(self):
        return self.__coordinates

    @coordinates.setter
    def coordinates(self, coords):
        i, j = coords
        self.__coordinates = (i, j)

    @coordinates.deleter
    def coordinates(self):
        del self.__coordinates

    @classmethod
    def count_cells(cls):
        print('There are {} cells'.format(cls.total_cells))
