from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

shape = Circle(5)
print("Площадь круга:", shape.calculate_area())
print("Периметр круга:", shape.calculate_perimeter())

shape = Rectangle(4, 6)
print("Площадь прямоугольника:", shape.calculate_area())
print("Периметр прямоугольника:", shape.calculate_perimeter())