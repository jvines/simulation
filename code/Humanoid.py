from Entity import Entity


class Humanoid(Entity):

    def __init__(self, i, j, field, cell, age):
        super().__init__(i, j, field, cell)
        self.alive = True

    def is_alive(self):
        return self.alive

    def kill(self):
        self.alive = False

    def eat(self):
        terrain_info = self.cell.terrain
        terrain_info.food
