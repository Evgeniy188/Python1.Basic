class Road:

    def __init__(self, l, w):
        self._length = l
        self._width = w

    def calc_asphalt(self, massa, n):
        return (self._length * self._width * massa * n) / 1000


road = Road(20, 5000)
print(road.calc_asphalt(25, 5))
