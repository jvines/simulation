import scipy as sp
import numpy.random as npr

class Terrain:

    possible_terrains = [
         'grass', 'dirt', 'water'
    ]

    def __init__(self, field, cell):
        self.field = field
        self.cell = cell
        self.terrain_type = '0'

    def init_terrain_cell(self):
        choice = npr.choice(Terrain.possible_terrains)
        self.terrain_type = choice

    def propagate_terrain(self):
        ady = self.get_adyacent_cells()

    def get_adyacent_cells(self):
        """Returns valid adyacent cells"""
        i, j = cell.coordinates
        field_size = (field.height, field.width)

        ady_i = [i - 1, i, i + 1]
        ady_j = [j - 1, j, j + 1]

        valid_ady = []

        # Check adyacent positions
        for ii in ady_i:
            for jj in ady_j:
                # Ignore current position
                if ii == i and jj == j:
                    continue
                # If adyacent coordinates are valid in the field, add them
                if self.field.is_valid_coord((ii, jj)):
                    valid_ady.append((ii, jj))
        return valid_ady
