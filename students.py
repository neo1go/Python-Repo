import csv


students = []  # dies ist nicht die Datei

with open("students.csv") as file:
    reader = csv.DictReader(file)  # dictreader anstatt reader. Damit wird die CSV Datei als dict behandelt.
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]}) # Der header in der csv Datei definiert somit die Key/value Paare der ganzen Datei.

"""
with open("students.csv") as file:    # 'with' dient wie 'using' in c# als statement, um nach der Schleife den Dateizugriff zu beenden bzw die Datei zu schließen.
    for line in file:
        name, home = line.rstrip().split(",")
        student = {"name": name, "home": home}  # hier erstellen wir ein Dictionary
        students.append(student)  #das dict wird in einer List gespeichert,damit man auf die keys zugreifen kann. Andernfalls würden ja keine Keys entstehen. 
   """     
        
        
"""        # dies ist eine Variante ohne die get_name Funktion:
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")
    
    """

"""
def get_name(student):         # Diese Get-Methoden können in dem for loop genutzt werden. Sie werden bei jedem Schritt des loops neu aufgerufen.
    return student["name"]     # Es gibt aber noch eine kürzere Schreibweise mit lambda, also einer anonymen Funktion.

def get_house(student):
    return student["house"]


# sorted kann man bei allen iterable Collections einsetzten. (list,tuple,str,set,dict)
for student in sorted(students, key=get_house, reverse=True): #students ist das dict, key muß angegeben werden, um damit richtig sortieren zu können.
    print(f"{student['name']} is in{student['house']}")

    """



# dies ist die kürzere Variante:
for student in sorted(students, key=lambda student: student["name"]): # lambda definiert eine anonyme Funktion, in diesem Fall student: student["name"]. student ist der Name
    print(f"{student['name']} is from {student['home']}")               # des Parameters. student["name"] ist der return Wert. Der return ist der Unterscheider und somit der key.
    


