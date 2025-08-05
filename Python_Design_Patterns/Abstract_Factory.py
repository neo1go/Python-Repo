from abc import ABC, abstractmethod

class IPizza(ABC):
    
    @abstractmethod
    def prepare_pizza():
        pass
    
class IDrink(ABC):
    
    @abstractmethod
    def serve_drink():
        pass
    
class American_Pizza(IPizza):
    def prepare_pizza(self):
        return 'American Pizza.'
        
class American_Drink(IDrink):
    def serve_drink(self):
        return 'Coca Cola.'
        
        
class Italian_Pizza(IPizza):
    def prepare_pizza(self):
        return 'Italian Pizza.'
        
class Italian_Drink(IDrink):
    def serve_drink(self):
        return 'Italian Vine.'
        
 
        
class IFood_Factory(ABC):
    
    @abstractmethod
    def create_pizza():
        pass
    
    @abstractmethod
    def create_drink():
        pass
    
    
    
class Italian_Factory(IFood_Factory):
    def create_pizza(self) -> IPizza:
        return Italian_Pizza()

    def create_drink(self) -> IDrink:
        return Italian_Drink()

class American_Factory(IFood_Factory):
    def create_pizza(self) -> IPizza:
        return American_Pizza()

    def create_drink(self) -> IDrink:
        return American_Drink()
        
        
        
        

def get_food_order(factory: IFood_Factory):  # factory ist eine konkrete Instanz einer der Klassen (z.B. Italian_Factory etc), die dann die Methoden implementieren.
    """
    Simuliert die Bestellung von Pizza und Getränken über eine Fabrik. Instanzen werden hier erstellt.
    """
    pizza = factory.create_pizza()
    drink = factory.create_drink()

    print(f"Ihre Bestellung: {pizza.prepare_pizza()} und {drink.serve_drink()}")
    print("-" * 30)



def main():
    """
    Hauptfunktion zur Demonstration der Abstract Factory Methode.
    """
    print("Bestellung von italienischem Essen:")
    get_food_order(Italian_Factory())   # hier sind Argumente eingetragen

    print("\nBestellung von amerikanischem Essen:")
    get_food_order(American_Factory())

# Der Einstiegspunkt des Skripts.
# Der Code in diesem Block wird nur ausgeführt, wenn das Skript
# direkt als Hauptprogramm gestartet wird (z.B. mit `python your_script.py`).
# Wird das Skript importiert, wird dieser Block übersprungen.
if __name__ == "__main__":
    main()