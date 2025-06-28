from random import randint
import time

def random_damage_multiplier():
    percentage = randint(0, 100)
    
    if percentage >= 90:
        return 2
    elif percentage >= 20:
        return 1
    else:
        return 0
    

def battle(sp1, sp2):
    attacker = sp1
    defender = sp2
    
    while sp1.alive and sp2.alive:
        weapon_damage = attacker.weapon.damage
        damage_mulitplier = random_damage_multiplier()
        damage = weapon_damage * damage_mulitplier
        
        name1 = attacker.nickname.upper()
        name2 = defender.nickname.upper()
        
        hp1 = attacker.health
        hp2 = defender.health
        
        if damage_mulitplier == 2:
            print(f"{name1}({hp1}) trifft {name2}({hp2}) mit {damage} (🔥KRITISCH 🔥).")
        elif damage_mulitplier == 1:
            print(f"{name1}({hp1}) trifft {name2}({hp2}) mit {damage} Schaden.")
        else:
            print(f"{name1}({hp1}) verfehlt...")
            
        attacker.attack(defender, damage_mulitplier)   # attack Methodenaufruf mit target und Faktor für die Multiplikation.
        
        if sp1.alive and sp2.alive:
            attacker, defender = defender, attacker  # Rollentausch.
        else:
            break
        
        time.sleep(0.3)
    
    if sp1.alive:
        print(f"{sp1.nickname} hat gewonnen.")
    else:
        print(f"{sp2.nickname} hat gewonnen.")