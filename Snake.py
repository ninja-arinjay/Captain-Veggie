from Creature import Creature


class Snake(Creature):
    def __init__(self, x, y):
        super().__init__(x, y, "S")

    def get_x(self):
        return self._x

    def set_x(self, x):
        self._x = x

    def get_y(self):
        return self._y

    def set_y(self, y):
        self._y = y
