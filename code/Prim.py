import numpy.random as npr

from Humanoid import Humanoid

DELTA_AGE = 1
DELTA_HUNGER = 1
MAX_AGE = 25
HUNGER = 50
MAX_HUNGER = 100
MIN_HUNGER = 0


class Prim(Humanoid):

    def __init__(self, name, i, j):
        super().__init__(i, j)
        self.__name = name
        self.age = age
        self.max_age = MAX_AGE + int(npr.normal(0, 5.5))
        self.hunger = HUNGER

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.age

    @age.setter
    def age(self, age):
        self.age = age

    def advance_age(self):
        self.age += DELTA_AGE
        self.hunger += DELTA_HUNGER
        if self.age >= self.max_age:
            self.kill()
        elif self.hunger > MAX_HUNGER:
            self.kill()

    def eat(self):
        if MIN_HUNGER < self.hunger:
            terrain_info = self.cell.terrain
