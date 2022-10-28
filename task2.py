class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.weight = 25
        self.height = 0.05

    def asphalt(self):
        asphalt = self._length * self._width * self.weight * self.height / 1000
        print(f"Для покрытия дорожного полотна нужно: {round(asphalt)} тонн асфальта")


r = Road(5000, 20)
r.asphalt()
