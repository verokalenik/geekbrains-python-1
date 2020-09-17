class Road:

    def __init__(self, length, width, weight):
        self._length = length
        self._width = width
        self._weight = weight

    def calc_overall_weight(self):
        return self._length * self._width * self._weight


r1 = Road(100, 5, 3)
print(r1.calc_overall_weight())

r2 = Road(300, 3, 2)
print(r2.calc_overall_weight())
