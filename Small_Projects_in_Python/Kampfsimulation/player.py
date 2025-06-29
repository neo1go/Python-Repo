class Player:

    def __init__(self, nickname, weapon):
        self.__nickname = nickname
        self.__health = 100
        self.__weapon = weapon

    @property # Getter
    def nickname(self):
        return self.__nickname

    @property # Getter
    def health(self): 
        return self.__health

    @property # Getter 
    def alive(self):
        return self.health > 0
    
    @property # Getter
    def weapon(self):
        return self.__weapon


    def attack(self, target, multiplier=1):
        damage = self.weapon.damage * multiplier
        target.get_damage(damage)  # hier wird get_damage direkt aufgerufen zur Berechnung auf dem Ziel.

    def get_damage(self, damage):  # Setter für __health, eine interne Klassenmethode, die Änderungen an __health vornehmen darf.
        self.__health -= damage
        if self.__health < 0:
            self.__health = 0
