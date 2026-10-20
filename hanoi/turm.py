# Die Klase dient mittels list und append() sowie pop() als Stackersatz

from scheibe import Scheibe


class Turm:
    def __init__(self, name: str):
        self.name = name 
        self.scheiben: list[Scheibe] = []
    
        

    def darf_ablegen(self, scheibe: Scheibe) -> bool:
        
        if len(self.scheiben) == 0:  # ein leerer Platz darf immer belegt werden
            return True
        
        oberste_scheibe = self.scheiben[-1]  # rechts in der list steht immer die oberste Scheibe
        
        if scheibe.groesse < oberste_scheibe.groesse:
            return True
    
        return False