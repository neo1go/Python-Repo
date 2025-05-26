

name = input("What's your name? ")


with open("names.txt","a") as file:   # w ist der Schreibmodus. Sollte die Datei noch nicht existieren, wird sie erstellt.
    file.write(f"{name}\n")           # a dient dem Anhängen, also append.     \n dient als linebreak nach jedem Speichern. Muß eingerückt werdeb
# alte Variante ist  file.close()

