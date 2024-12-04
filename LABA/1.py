import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius ** 2


class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


class InscribedCircle(Circle, Square):
    def __init__(self, side):
        radius = side / 2
        Circle.__init__(self, radius)
        Square.__init__(self, side)

    def info(self):
        return {
            "Circle Radius": self.radius,
            "Circle Circumference": self.circumference(),
            "Circle Area": self.area(),
            "Square Side": self.side,
            "Square Area": self.area()
        }


# Пример использования
side_length = 4
inscribed_circle = InscribedCircle(side_length)

print("Информация о окружности и квадрате:")
for key, value in inscribed_circle.info().items():
    print(f"{key}: {value}")
