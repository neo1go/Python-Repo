# Template Pattern 
# Macht besonders dann Sinn, wenn sich Klassen und deren Methoden kaum unterscheiden
# und mittels Überschreiben austauschbar sind wie in diesem Fall brew() und add_condiments().
from abc import ABC, abstractmethod

# Template
class CaffeineBeverage(ABC):
    
    def prepare_recipe(self):       # dieser Ablauf ist für beide Klassen gleich.
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        if self.customer_wants_condiments():
            self.add_condiments()
        print("-" * 30)

    def boil_water(self):   # Konkret, weil für beide Getränke gleich.
        print("Wasser wird gekocht")

    @abstractmethod
    def brew(self):
        pass

    def pour_in_cup(self):   # Konkret, weil für beide Getränke gleich.
        print("In die Tasse gegossen")

    @abstractmethod
    def add_condiments(self):
        pass

    # Hook – optionaler Schritt
    def customer_wants_condiments(self):
        return True


# Konkrete Implementierung: Tee
class Tea(CaffeineBeverage):
    def brew(self):
        print("Tee wird aufgebrüht")

    def add_condiments(self):
        print("Zucker und Zitrone hinzugefügt")



# Konkrete Implementierung: Kaffee
class Coffee(CaffeineBeverage):
    def brew(self):
        print("Kaffee wird gebrüht")

    def add_condiments(self):
        print("Milch und Zucker hinzugefügt")

    # Hook überschreiben – optional
    def customer_wants_condiments(self):
        return False  # keine Gewürze/Zutaten


def main():
    
    def beverage_generator():
        yield Tea()         # lazy Instanziierung
        yield Coffee()
        
    
    for beverage in beverage_generator(): # Instanzen werden somit nur bei Bedarf erstellt
        beverage.prepare_recipe()

    
# Kurzschreibweise mit Comprehension, bei der keine Generator-Methode benötigt wird.
   # for beverage in (b() for b in [Tea, Coffee]):
   # beverage.prepare_recipe()



if __name__ == "__main__":
    main()