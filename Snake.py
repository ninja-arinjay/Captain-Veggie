from Creature import Creature

class Snake(Creature):
    def _init_(self, x, y):
        super()._init_(x, y, "S")