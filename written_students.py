import csv

name = input("Whats your name? ")
home = input("Where's your home? ")

with open("writtenStudents.csv", "a", newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})


