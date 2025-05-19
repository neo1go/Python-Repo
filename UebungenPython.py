import math  
import datetime
import json
#-------------------------------------------------
# # List Sort
# d = [12, 2, 3, 4, 5]
# d.sort()
# for x in d:
#     print(x)

# # mehrfache Ausgabe des chars durch Multiplikator
# print("z"*10)
#-------------------------------------------------
# #Strings
# course = "Python Programming"
# print(len(course))
# print(course[1])
# print(course[-1])  # letzter char des strings
# print(course[0:6])  # slicing
# print(course[7:])
# print(course[:])  # Kopie des originalen Strings

# print('Dies lässt einen ein Anführungzeichen " anzeigen')
# print("Dies lässt einen ein Anführungzeichen \" anzeigen")   # escape-sequence
# dies sind weitere Escape Sequenzen
# \"
# \'
# \\
# \n    erstellt eine new line

#-------------------------------------------------
# # Konkatenierung von strings
# first = "  Gordon"
# last = "H  "
# full = first + " " + last # kann man mit interpolation einfacher schreiben
# fuller = f"{first} {last}  {49+1}"  #string interpolation, also formatted string mit f
# course = "Python Programming"
# print(fuller.upper())
# print(fuller) #der originale String wurde nicht verändert
# print(fuller.title())
# print(fuller.strip()) # es gibt auch lstrip für leftstrip oder rstrip für rightstrip
# print(course.find("Pro"))   # Achtung -> case sensitive. Zeigt den index an.
# print(course.replace("P","j"))
# print("Pro" in course)  # Expression -> also Code, der einen Wert produziert, in diesem Fall einen boolean.
# print("swift" not in course)

#-------------------------------------------------
# Numbers

# x = 1  # int
# x = 1.1  # float, also Kommazahlen
# x = 1 + 2j  # complex, hauptsächlich für mathematische Berechnungen. j ist im mathematischen Bereich eigentlich i, wird aber beim Programmieren
#           # als j dargestellt. (x=a+bi) (x=real+imagr)
# print(10 + 3)
# print(10 - 3)
# print(10 * 3)
# print(10 / 3)
# print(10 // 3) # die Zahl wird abgerundet
# print(10 % 3) #modulo ist der Restwert einer Division
# print(10 ** 3) # Exponent, also zehn hoch drei 

# x = 10
# x = x + 3
# x += 3  # diese beiden Statements sind identisch

# print(round(2.9)) # rundet rcihtig auf oder ab
# print(abs(-10)) # gibt immer positiven Wert zurück

# help(math)    # dieser Befehl ziegt alle Erklärungen zu einem Modul im Terminal an.

# x = input("Die Zahl x: ")   # nimmt einen Input vom User im Terminal an 
# print(f"Der Datentyp von x ist {type(x)}") # zeigt den Datentyp an.
# y = int(x) + 1              # boxing oder Typkonvertierung genannt. 
# print(f"Nun ist der Datentyp von y ein {type(y)}")
# print(y)
#-------------------------------------------------
# Boolean

# Diese Rückgaben sind alle Falsy, alles andere ist True. Dies bezieht sich im Moment auf strings.
# ""
# 0
# None


#-------------------------------------------------
# primitive types in Python
# strings
# numbers (int,float,complex)
# booleans

# Ausgabe des ASCII Wertes in der Konsole mit ord
# print(ord("0")) 

#-------------------------------------------------
# Conditional Statements

# temperature = 15
# if temperature > 30:
#     print("It's warm")
#     print("Drink water")
# elif temperature > 20:
#     print("It's nice")
# else:
#     print("It's cold")
# print("Done")



#-------------------------------------------------
# Tenary Operator

# age = 22
# if age >= 18:
#     message = "Eligible"
# else:
#     message = "Not eligible"   
# print(message)

# #kürzere Einzeiler-Variante
# message2 = "Eligible" if age >= 18 else "Not eligible"  #tenärer Operator
# print(message2)


#-------------------------------------------------
# Logical Operators

# high_income = False
# good_credit = True
# student = True

# if high_income and good_credit:
#     print("Eligible")
# else:
#     print("Not eligible")

# if high_income or good_credit:
#     print("Eligible")
# else:
#     print("Not eligible")
    
# if not student:
#     print("Eligible")
# else:
#     print("Not eligible")

# if (high_income or good_credit) and not student:
#     print("Eligible")
# else:
#     print("Not eligible")
    
# if high_income or good_credit and not student:
#     print("Eligible")
# else:
#     print("Not eligible")

#-------------------------------------------------

# Chaining comparison operators
# age = 22
# if 18 <= age < 65:
#     print("Eligible")
    
# if 10 == "10": # int und string sind nicht identisch
#     print("a")
# elif "bag" > "apple" and "bag" > "cat":  # (bag kommt nach apple und ist somit größer) aber (cat kommt nach bag und das Statement ist false)
#     print("b")
# else:
#     print("c")

#-------------------------------------------------

# Loops

# for number in range(1, 10, 2):
#     print("Attempt", number, number * ".")  # number ist der Index des loops

#-------------------------------------------------

# For Else
# successful = False 
# for number in range(3):
#     print("Attempt", number +1)
#     if successful:
#         print("Successful")
#         break
# else:
#     print("Attempted 3 times and failed")

#-------------------------------------------------

# Nested Loops

# for x in range(5):
#     for y in range(3):       # child
#         print(f"({x}, {y})")

#-------------------------------------------------

# Iterables

# print(type(5))   # class int
# print(type(range(5)))  # returned ein object vom typ range, das iterable ist.

# for x in "Python":     # strings sind auch iterable.
#     print(x)

# for x in [1,2,3,4]:  #[]Eckige Klammern sind List, ()runde Klammern sind tuple und {}geschweifte Klammern sind set oder dict. 
#     print(x)

#-------------------------------------------------

# While loops

# number = 100
# while number > 0:
#     print(number)
#     number //= 2    # abgerundetes Dividieren

# command = ""
# while command.lower() != "quit":  # lower() wandelt den gesamten Input um, so dass man nicht verschiedene Eingabarten prüfen muss.
#     command = input(">")
#     print("ECHO", command)
  
# andere Variante des selben Codes
# while True:   # endless loop bis zur Break-Bedingung
#     command = input(">")
#     print("ECHO", command)
#     if command.lower() == "quit":
#         break  
    
# count = 0
# for i in range(10):
#     if i %2 == 0 and i > 0:
#         count += 1
#         print(i)
# print(f"We have {count} even numbers")

# for i in range(1,10):
#     if i %2 == 0:
#         count += 1
#         print(i)
# print(f"We have {count} even numbers")

#-------------------------------------------------

# Methods, (Functions)

# 2 Arten von Funktionen
# Funktionen, die eine Aufgabe ausführen.
# Funktionen, die einen Wert zurückgeben.

# def greet(name):   #Parameter
#     print(f"Hi there, {name} ")
    
# greet("Gordon")    # hier werden die eigentlichen Argumente übergeben.

# def get_greeting(name): # diese Funktion gibt einen Wert zurück mittels 'return'. Die 2 Variante ist zu bevorzugen da sie einen Wert zurückgibt, mit dem man dann weiterabeiten kann.
#     return f"Hi {name}"

# message = get_greeting("Pete")
# print(message)
# file = open("content.txt", "w")  # w für write.   ACHTUNG, die Datei content.txt wird einfach erstellt mittels open.
# file.write(message)   # Einfügen der Message in die Datei. Dies funktioniert nur, wenn man vorher w ausgewählt hat. Mit r wäre sie nur lesbar.

#-------------------------------------------------

# def increment(number, by):
#     return number + by


# print(increment(2, by=1))  # 'by' ist ein keyword-argument

# def optional_increment(number, by=1):     # wenn der Parameter einen Default-Parameter zugewiesen bekommen hat, ist eine Übergabe optional, da schon ein Wert existiert.
#     return number + by    # Optionale Parameter müßen immer hinter den zwingenden Parametern stehen in der Parameterliste.


# print(optional_increment(2))

#-------------------------------------------------

# XARGS -> Mit Methoden multiple Argumente benutzen

# def multiply(*numbers):   # es wird quasi eine List an Argumenten übergeben, deswegen das Asterix als Platzhalter.
#     total = 1
#     for number in numbers:
#         total *= number
#     return total

# print(multiply(2,3,4,5))

#-------------------------------------------------

# Datetime Bearbeitung ,dazu muß man datetime importieren

# time = datetime.datetime
# print(time.now())

# weekday = datetime.datetime.now()
# print(weekday.strftime('%A'))   # gibt den Tag an alr Reinname wie z.B. Monday, Tuesday etc.

# month = datetime.datetime.now()
# print(month.strftime('%B'))  # gibt den Monat aus (full version) wie z.B. May, June, July etc.

# x = datetime.datetime(2024, 8, 20)
# print(x.strftime('%d'))   # gibt den Tag an. Das Format ist ja YYYY,MM,dd. Mit dem % werden die anderen Werte gescliced.

#-------------------------------------------------

# Weitere Math-Funktionen

# print(max(5,10,25))
# print(pow(2,3))   # 2 hoch 3, also potenzieren
# print(math.sqrt(9))  # Wurzel ziehen
# print (math.pi)   

#-------------------------------------------------

# JSON Bearbeitung

# data = {                                #  dies ist im Moment ein dict mit key-value Paaren.
#     "name" : "Dieter",
#     "age" : 25,
#     "tel" : "02345"
# }
# json_string = json.dumps(data)

# for key, value in data.items():
#     print(key, ":", value)

#-------------------------------------------------

# mit venve lassen virtuelle Umgebungen erstellen
# mit deactivate wird solch eine Umgebung wieder ausgeschaltet.
# um eine virtuelle Umgebung zu erstellen, scheibt man "python -m venv mytest" im terminal.

#-------------------------------------------------

# mot open() lassen sich Dateien öffnen oder auch neu erstellen falls diese Datei noch nicht existiert.
# x = open('demofile.txt', 'b')# dies öffnet die Datei im binary mode, "r" für reading, ACHTUNG -> "w" für write. Dies überschreibt.
# Dann kann man mit read() die Datei lesen.

# wenn man nur eine Zeile lesen möchte, dann nutzt man    readline()
# um so öfter readline() hintereinander aufgerufen wird, um so mehr Zeilen werden ausgelesen.

# wenn man "x" einsetzt, wird einem ein eventueller Fehler auch gemeldet.

# um Dateien zu löschen, benötigt man das os Modul.
# mit    os.remove() lassen sich Dateien löschen.
# mit    os.rmdir()  wird ein ganzer Ordner gelöscht.
# Achtung, um einen Ordner mit os zu löschen, muß dieser leer sein!!!!!


