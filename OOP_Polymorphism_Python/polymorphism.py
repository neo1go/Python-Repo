# Polymorphismus = Vielgestaltigkeit 
# In Python gibt es 2 Möglichkeiten, um Polymorphie zu erreichen:
# 1. Vererbung = das Objekt wird genauso behandelt wie ein vergleichbares Objekt der Elternklasse. -> Square oder Triangle oder Circle erben von Shape.
# 2. "duck typing" = das Objekt muß die nötigen Attribute und/oder Methoden haben. -> Pizza besitzt radius und kann somit die Circle Klasse bedienen.
from abc import ABC, abstractmethod


class Shape:
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side
        
    def area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
        
    def area(self):
        return self.base * self.height * 0.5
        
        
class Pizza(Circle):
    def __init__(self, topping, radius):
        super().__init__(radius)
        self.radius = radius

        
        
shapes = [Circle(4),Square(5), Triangle(6, 7), Pizza("pepperoni", 15)]

for shape in shapes:
    print(f"{shape.area()}cm²")  # ALT + 0178 für das Quadratzeichen