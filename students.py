students = []


with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)
        
        
        
"""        # dies ist eine Variante ohne die get_name Funktion
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")
    
    """

def get_name(student):
    return student["name"]

def get_house(student):
    return student["house"]


for student in sorted(students, key=get_house, reverse=True):           #key muß angegeben werden, um damit richtig sortieren zu können.
    print(f"{student['name']}is in{student['house']}")

