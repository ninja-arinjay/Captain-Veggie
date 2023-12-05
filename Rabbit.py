from Creature import Creature


class Rabbit(Creature):
    def __init__(self, x, y):
        super().__init__(x, y, "R")

    def get_x(self):
        return super().get_x()

    def set_x(self, x):
        super().set_x(x)

    def get_y(self):
        return super().get_y()

    def set_y(self, x):
        super().set_y(x)
