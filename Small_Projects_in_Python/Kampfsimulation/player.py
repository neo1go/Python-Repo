class Player:

    def __init__(self, nickname, weapon):
        self.__nickname = nickname
        self.__health = 100
        self.weapon = weapon

    @property
    def nickname(self):
        return self.__nickname

    @property
    def health(self):
        return self.__health

    @property
    def alive(self):
        return self.health > 0

    def attack(self, target, multiplier=1):
        damage = self.weapon.damage * multiplier
        target.get_damage(damage)  # hier wird get_damage direkt aufgerufen zur Berechnung auf dem Ziel.

    def get_damage(self, damage):
        self.__health -= damage
        if self.__health < 0:
            self.__health = 0
