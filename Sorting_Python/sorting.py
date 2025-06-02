# .sort() Method auf ein Objekt oder die sorted() Funktion.
# Sorting wird zum Sortieren von Lists[], Tupeln(), Dicts{"":""} oder Objekten verwendet

#-----------Lists------------
fruits = ["banana","orange","apple","coconut"]
nums = [1,5,3,8,12,4]

fruits.sort()
nums.sort(reverse=True)  # so kann man rückwärts sortieren

print(fruits)
print(nums)




#----------Tuples-------------
# tuples sind feststehend und können nur erweitert werden

t_fruits = ("banana","orange","coconut","apple")

#new_t_fruits = sorted(t_fruits, reverse=True)  # hier wird umgewandelt in eine List
new_t_fruits = tuple(sorted(t_fruits))  # so wird die Tuple-Struktur beibehalten mittels typecasting

print(new_t_fruits)




#---------Dictionaries---------
d_fruits = {"banana": 105,
            "orange": 73,
            "apple": 72,
            "coconut": 354}

#d_fruits = sorted(d_fruits)  # dies ist nur eine List und verliert somit auch die Values.
key_fruits = dict(sorted(d_fruits.items()))    # items macht aus dem Eintrag jeweils eín tuple und dict behält die Dictionary-Struktur bei.
print(key_fruits)

rev_fruits = dict(sorted(d_fruits.items(), key=lambda item: item[0], reverse=True)) # es muß 0 oder 1 ausgewählt werden um zu entscheiden, nach welchem Eintrag des Dict
# die sorted Funktion agieren soll, in diesem Fall entweder 0 für den Key oder 1 für die Value. Erst dann kann sorted auch ausgeführt werden.
print(rev_fruits)


val_fruits = dict(sorted(d_fruits.items(), key=lambda item: item[1]))   # nach value sortiert. Für mich ist lambda in diesem Fall der Pointer auf die Stelle, die verglichen
                                                                        # werden soll. Die [1] ist die Value im key/value Eintrag.
print(val_fruits)




#-----------CLass-Objects----------------

class Fruit:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories
        
    def __repr__(self):   # dies wird jedesmal beim print() aufgerufen. repr=represent ist hier also von uns abgewandelt.
        return f"{self.name}: {self.calories} cal"


class_fruits = [Fruit("banana", 105),
                Fruit("apple", 72),
                Fruit("orange", 73), 
                Fruit("coconut", 354)]


c_fruits = sorted(class_fruits, key=lambda fruit: fruit.name, reverse=True)  # .name ist der Sortierwert, an dem sich orientiert wird.
cal_fruits = sorted(class_fruits, key = lambda fr: fr.calories)

print(c_fruits)
print(cal_fruits)