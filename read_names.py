namesList = []

with open("names.txt") as file:          # "r" is default
    for line in file:
        namesList.append(line.rstrip())  # es wird die neue Liste befüllt, um sie anschließend zu sortieren.
                                         # dies könnte man zusammenfassen mit sorted(file)und append weglassen,
                                         # aber so kann man modularer arbeiten.
                                         
for name in sorted(namesList,reverse=True):          # hier wird sortiert.
    print(f"hello, {name}")