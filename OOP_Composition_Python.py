# Komposition ist eine Beziehung von Objekten zueinander, bei der das zusammengesetzte Objekt durch die Komponenten erstellt wird. 
# Das zusammengesetzte Objekt besitzt ("owns a" Relationship) die Komponenten und es kann nicht ohne diese Komponenten existieren sowie
# die Komponenten nicht ohne das Ganze existieren kann. Bspl.: Haus und Räume, Mensch und Organe, Buch und Seiten.


class Engine:
    def __init__(self, horse_power):
        self.horse_power = horse_power
        
        
class Wheel:
    def __init__(self, size):
        self.size = size
        
        
class Car:
    def __init__(self, make, model, horse_power, wheel_size):
        self.make = make
        self.model = model
        self.engine = Engine(horse_power)   # dies sind die Kompositionen für engine und wheels. Car besitzt engine und wheels. 
        self.wheels = [Wheel(wheel_size) for wheel in range(4)] 
                
    def display_car(self):
        return f"{self.make} {self.model} {self.engine.horse_power}(hp) {self.wheels[0].size}(inches)"



car1 = Car("Ford", "Mustang", 500, 18)
car2 = Car("Chevrolet", "Corvette", 670, 19)


print(car1.display_car())
print(car2.display_car())

# Wenn man hier die car Objekte zerstören würde, würden die Engine und Wheel Objekte aufhören zu existieren in diesem Kontext.