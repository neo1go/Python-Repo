# Statische Methoden gehören zur Klasse selbst und nicht zum Objekt oder der Instanziierung.
# Sie werden meist für generelle Aufgaben genutzt.

# Instance Methods = Best for operations on instances of the class (objects)
# Static methods = Best for utility functions that do not need access to class data

class Employee:
    
    def __init__(self, name, position):
        self.name = name
        self.position = position
        
    def get_info(self):
        return f"{self.name} = {self.position}"
    
    @staticmethod
    def is_valid_position(position):   # es wird kein self übergeben
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions #gibt True oder False zurück
    
    
employee1 = Employee("Eugene","Manager")
employee2 = Employee("Squidward","Cashier")
employee3 = Employee("Spongebob","Agent")

    
    
print(Employee.is_valid_position("Gurke"))
print(Employee.is_valid_position("Manager"))

print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())

# dies ist ein Umweg der wenig Sinn macht, da man dann die Methode wohl eher nicht statisch setzen sollte.
print(Employee.is_valid_position(employee1.position))
print(Employee.is_valid_position(employee2.position))
print(Employee.is_valid_position(employee3.position))