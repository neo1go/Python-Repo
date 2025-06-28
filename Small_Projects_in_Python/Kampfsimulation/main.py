from player import Player
from utils import battle
from weapon import Weapon

weapon1 = Weapon("Kurzschwert", 12)
weapon2 = Weapon("Axt", 14)

player1 = Player("Leonidas", weapon1)
player2 = Player("Herkules", weapon2)

battle(player1,player2)  