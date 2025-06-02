# abstract classes define abstract methods that function as a template without the proper implementation.
# These classes can't be instanciated. It compels the developer to override the method in a child class.

from abc import ABC, abstractmethod   # abc = abstract base class, abstractmethod ist der Decorator den wir nutzen wollen.

class Vehicle(ABC):              # es wird aus der Library dann ABC übergeben, damit man die Klasse als abstrakt deklarieren kann.
    @abstractmethod              # dies ist nun eine abstrakte Methode durch den Decorator
    def go(self):
        pass
    @abstractmethod
    def stop(self):
        pass
    
    def honk(self):   # diese Methode kann nicht auf Vehicle genutzt werden da Vehicle selbst abstrakt ist. Kindklassen können diese Methode 
        print("Honk") # aber trotzdem nutzten.

class Car(Vehicle):
    def go(self):
        print("You drive a car")
    
    def stop(self):
        print("This car is stopped.")   

        
class Motorcycle(Vehicle):
    def go(self):
        print("Your ride a motorcycle")
     
    def stop(self):
        print("This motorcycle is stopped.")   
        

car = Car()
motorcycle = Motorcycle() 

car.honk()        # dies ist eine konkrete Methode der abstrakten Klasse Vehicle, die trotzdem auf Kindklassenobjekte
motorcycle.honk() # von Vehicle angewandt werden kann.

car.go()
motorcycle.go()

car.stop()
motorcycle.stop()
