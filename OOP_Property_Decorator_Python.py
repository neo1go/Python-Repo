# @property = Dieser Decorator definiert eine Methode als eine Eigenschaft. Es kann also auf die Methode genauso 
# zugegriffen werden wie auf eine normale Eigenschaft.
# Dadurch kann man Logiken hinzufügen wenn man Attribute lesen, schreiben oder löschen möchte.
# Man erhält eine getter, setter und deleter Methode.

# ACHTUNG Dies ist keine Überladung wie in anderen Prgrammiersprachen sondern es ermöglicht nur die Verwendung von Getter, Setter und Deleter
# auf einer definierten Eigenschaft, in diesem Fall width und height.


class Rectangle:
    def __init__(self, width, height):
        self._width = width    # ein underscore heißt protected und zwei Underscore heißt private
        self._height = height
     
    @property                               # wie ein Getter
    def width(self):
        return f"{self._width:.1f}cm"
    
    @property
    def height(self):       
        return f"{self._height:.1f}cm"
    
    @width.setter           # Setter 
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than zero")
            
    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be greater than zero")
    
    @width.deleter  # Deleter
    def width(self):
        del self._width
        print("Width has been deleted.")
        
    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted.")
    
rectangle = Rectangle(3, 4)

rectangle.width = 0
rectangle.height = -1

del rectangle.width
del rectangle.height
 