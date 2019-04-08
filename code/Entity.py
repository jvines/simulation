import scipy as sp
import numpy.random as npr


class Entity:

    total_entities = 0

    def __init__(self, i, j, field, cell):
        self.__coordinates = (i, j)
        self.field = field
        self.cell = cell
        cls.total_entities += 1

    @property
    def coordinates(self):
        return self.__coordinates

    @coordinates.setter
    def coordinates(self, coord):
        i, j = coord
        self.__coordinates = (i, j)

    @coordinates.deleter
    def coordinates(self):
        del self.__coordinates

    @classmethod
    def count_entities(self):
        print('There are {} entities.'.format(cls.total_entities))
