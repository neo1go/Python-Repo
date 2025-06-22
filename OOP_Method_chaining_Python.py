# mit Method Chaining kann man Methoden sequenziell aneinander reihen, wenn sie das Objekt kennen, das sie bearbeiten sollen, egal ob in der gleichen oder einer anderen Klasse.
# Die Methoden müssen dabei immer ein Objekt returnen, andernfalls weiß beim Chainen die nächste Methode nicht, mit welchem Objekt sie arbeiten soll.


class Car:
    def turn_on(self):
        print("You start the engine")
        return self
    
    def drive(self):
        print("You drive the car")
        return self
    
    def brake(self):
        print("You step on the brakes")
        return self
    
    def turn_off(self):
        print("You turn off the engine")


car = Car()

 #car.turn_on().drive().brake().turn_off() 
 
# der backslash ist ein line continuation-character. ACHTUNG - Es dürfen keine Leerzeichen hinter dem backslash sein, weil diese nicht ignoriert werden wie sonst. 
 
car.turn_on()\
    .drive()\
    .brake()\
    .turn_off()