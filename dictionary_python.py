# Das dict ist eine collection von key value Paaren die sortiert und änderbar sind.
# Die Keys sind einzigartig, also keine Duplikate.

capitals = {"USA" : "Washington",
            "India" : "New Dehli",
            "China" : "Beijing",
            "Russia" : "Moscow"}

# print(dir(capitals))  # dir zeigt alle Methoden und Attribute eines Dictionaries
# print(help(capitals))  # zeigt alle Methoden genauer an als dir.

# print(capitals.get("USA"))


# if capitals.get("Russia"):
#     print("That capital exists.")
# else:
#     print("Not found.")
    
# capitals.update({"Germany" : "Berlin"})
# capitals.update({"USA" : "Detroit"})     # überschreibt den vorherigen Wert wenn der key schon existierte.
# capitals.pop("China")  # hiermit wird ein ausgesuchter key und somit auch die Value mitgelöscht.

# capitals.popitem() # schmeißt immer den letzten Eintrag des Dictionaries raus.

# capitals.clear()  # öeert das ganze Dictionary

# keys = capitals.keys()
# values = capitals.values()

# for key in keys:
#     print(key)

# for value in values:
#     print(value)

for key, value in capitals.items():   # items gilt für ein ganzes Paar. So kann man key und value gemeinsam leicht anzeigen. 
    print(f"key: {key}, value: {value}")