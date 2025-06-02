# filter(function, collection)  gibt alle Elemente zurück, die eine Bedingung erfüllen. Die Bedingung kann auch als lambda geschrieben sein.

def is_passing(grade):
    return grade >= 60

grades = [91, 32, 83, 44, 75, 56, 67]



passing_grades = filter(is_passing, grades)#Filter vergleicht zwischen der Bedingung in der Funktion und der zugrundeliegenden Collection.
for grade in passing_grades:
    print(f"normal Version: {grade}")
    
#passing_grades = list(filter(is_passing, grades))   #typecasting zu List
#print(passing_grades)   # mittels Typecasting kann man dann sofort ausgeben.

lambda_version_passing_grades = filter(lambda gr: gr >= 60, grades)
for lvpg in lambda_version_passing_grades:
    print(f"Lambda Version: {lvpg}")