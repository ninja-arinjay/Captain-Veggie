from Creature import Creature


class Captain(Creature):
    def __init__(self, x, y):
        super().__init__(x, y, "V")
        self._veggies_collected = []

    def get_x(self):
        return super().get_x()

    def set_x(self, x):
        super().set_x(x)

    def get_y(self):
        return super().get_y()

    def set_y(self, x):
        super().set_y(x)

    def addVeggie(self, veggie):
        self._veggies_collected.append(veggie)

    def get_veggies_collected(self):
        return self._veggies_collected
