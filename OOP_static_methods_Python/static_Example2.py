from typing import Self
from datetime import date



class Calculator:
    def __init__(self, version: int):
        self.version = version
        
    def description(self):
        print(f"Currently running Calculator on version : {self.version}")
        
    @staticmethod      # kann überall geschrieben werden, auch außerhalb der Klasse. Kann ohne Objektinstanz genutzt werden.
    def add_numbers(*numbers: float) -> float:
        return sum(numbers)
   
   
   
   

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def descript(self) -> str:
        return f'{self.name} is {self.age} years old.'
        
    @classmethod
    def age_from_year(cls, name: str, birthyear: int) -> Self:  # hier wird durch cls ein alternativer Konstruktor angesprochen
        current_year: int = date.today().year
        age: int = current_year - birthyear
        return cls(name, age)

if __name__ == '__main__':
    
    calc1 = Calculator(10)
    calc2 = Calculator(200)
    
    calc1.description()
    calc2.description()
    
    print(Calculator.add_numbers(10,20,30))
    
    gordon = Person.age_from_year('Gordon', 1975)
    
    print(gordon.descript())