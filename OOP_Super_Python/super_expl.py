# super() = Ist eine Funktion die dazu dient, auf die Methoden der Superklasse zuzugreifen.
# Es wird ein temporäres Objekt der Elternklasse zurückgegeben, wenn super() genutzt wird.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
        
class Square(Rectangle):
    def __init__(self, length, width):
        super().__init__(length, width)   # um nicht immer die beiden Attribute jedesmal neu zu setzen, werden sie von der Elternklasse übernommen.
                                          # Es wird der Konstruktor der Elternklasse referenziert mit super().__init__
    def area(self):
        return self.length*self.width
    
    
class Cube(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height
    
    def volume(self):
        return self.length*self.width*self.height
   
    
square = Square(3, 3)
cube = Cube(3, 3, 3)

print(square.area())
print(cube.volume())