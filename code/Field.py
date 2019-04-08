import scipy as sp
import numpy.random as npr
from Terrain import Terrain
from Cell import Cell
from Entity import  Entity
from Humanoid import Humanoid
from Prim import Prim


class Field():
    """A field of the simulation.

    The field contains information for terrain and cells which holds entities
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.create_field()
        self.init_field_terrain()

    def __repr__(self):
        rep = sp.zeros((self.height, self.width), dtype=str)
        for i in range(self.height):
            for j in range(self.width):
                rep[i, j] = self.field[i, j].terrain.terrain_type[0]
        return rep.__repr__()

    def create_field(self):
        """Creates an empty field."""
        self.field = sp.empty((self.height, self.width), dtype=object)
        for i in range(self.height):
            for j in range(self.width):
                self.field[i, j] = Cell(i, j, self)

    def init_field_terrain(self):
        """Seeds the field with random terrain values."""
        # The initial seeded terrain is the 10% of the total cell number.
        # If the number is 0, then there is only one seed
        n = sp.floor(self.width * self.height * 0.2)
        seed_n = n if n > 0 else 1

        # Generate a random position and give that cell a random terrain value
        used_idxs = []
        while len(used_idxs) < seed_n:
            i, j = npr.randint(0, self.height), npr.randint(0, self.width)
            if (i, j) not in used_idxs:
                used_idxs.append((i, j))
                c = self.field[i, j]
                c.terrain.init_terrain_cell()

    def fill_terrain(self):
        pass

    def clear_field(self):
        """Clears the field."""
        for i in range(self.height):
            for j in range(self.width):
                del self.field[i, j]

    def is_valid_coord(self, coord):
        """Checks if a coordinate is valid in the field."""
        i, j = coord
        if 0 < i < self.width and 0 < j < self.height:
            return True
        return False
