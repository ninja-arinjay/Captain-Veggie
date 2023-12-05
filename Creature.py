from FieldInhabitant import FieldInhabitant


class Creature(FieldInhabitant):
    def __init__(self, x, y, symbol):
        super().__init__(symbol)
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def set_x(self, x):
        self._x = x

    def get_y(self):
        return self._y

    def set_y(self, y):
        self._y = y
