# Duck typing = Eine andere Art um Polymorphismus zu erreichen neben normaler Vererbung
# Das zu erzeugende Objekt muß zumindest die nötigen Attribute/Methoden besitzen um in der entsprechenden Collection valide zu sein. 


class Animal:
    alive = True
    

class Dog(Animal):
    def speak(self):
        print("Woof!")
        
        
class Cat(Animal):
    def speak(self):
        print("Miau!")


class Car:
    alive = False   # Klassenattribut (dadurch wird die Polymorphie quasi zulässig weil dieses Attribut noch fehlte.)
    
    def speak(self):   # dies funktioniert, ist aber eher ungünstig.
        print("Honk")


animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)