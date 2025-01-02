import math
class Figure:
    def __init__(self, color, *sides):
        self._color = color
        self._sides = [1] * self.sides_count if len(sides) != self.sides_count else list(sides)
    @property
    def sides_count(self):
        return 0
    def get_color(self):
        return self._color
    def _is_valid_color(self, r, g, b):
        return all([isinstance(x, int) and 0 <= x <= 255 for x in (r, g, b)])
    def set_color(self, r, g, b):
        if self._is_valid_color(r, g, b):
            self._color = (r, g, b)
    def _is_valid_sides(self, new_sides):
        return (
            len(new_sides) == self.sides_count and
            all(isinstance(side, int) and side > 0 for side in new_sides)
        )
    def get_sides(self):
        return self._sides
    def set_sides(self, *new_sides):
        if self._is_valid_sides(new_sides):
            self._sides = list(new_sides)
    def __len__(self):
        return sum(self._sides)

class Circle(Figure):
    sides_count = 1
    def __init__(self, color, radius):
        super().__init__(color, radius)
        self._radius = self._sides[0]
    def get_radius(self):
        return self._radius
    def get_square(self):
        return math.pi * self._radius ** 2

class Triangle(Figure):
    sides_count = 3
    def get_square(self):
        a, b, c = self._sides
        p = (a + b + c) / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))

class Cube(Figure):
    sides_count = 12
    def __init__(self, color, edge_length):
        super().__init__(color, *(edge_length for _ in range(self.sides_count)))
    def get_volume(self):
        edge_length = self._sides[0]
        return edge_length ** 3

# Код для проверки:
circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())