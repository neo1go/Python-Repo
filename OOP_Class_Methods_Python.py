# Klassenmethoden sind Methoden, die direkt auf die Klasse angewendet werden können ohne eine Objektinstanz zu erzeugen.
# Die Methode wird mit einem decorator @classmethod versehen und in der Parameterliste wird anstatt "self" für die Instanzierungsmethoden 
# das Kürzel cls verwendet(Konvention).

# Instanzmethoden werden genutzt, um instanziierte Objekte zu bearbeiten.
# Klassenmethoden werden genutzt, um auf Daten der Klasse zuzugreifen oder Operationen direkt auf der Klasse auszuführen.
# Statische Methoden werden als unabhängige Methoden verwendet, die keinen Zugriff auf Klassenobjekte benötigt.


class Student:
    
    count  = 0
    total_gpa = 0
    
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1  # count ist eine Klassenvariable und der Klasse angehörig und nicht direkt den Objektintanzen.
        Student.total_gpa += gpa
    # Instanzmethode   
    def get_info(self):
        return f"{self.name} {self.gpa}"
    
    #Klassenmethode, die auf Klassenvariablen zugreifen kann.
    @classmethod
    def get_count(cls):
        return f"total # of students {cls.count}"
    
    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average gpa: {cls.total_gpa / cls.count:.2f}"
  
  
student1 =  Student("Spongebob", 3.2) 
student2 =  Student("Patrick", 2.0) 
student3 =  Student("Sandy", 4.0) 
  
    
print(Student.get_count())

print(Student.get_average_gpa())