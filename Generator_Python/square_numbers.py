def square_numbers(nums):
    for n in nums:
        yield(n*n)       # dies ist immer nur ein Zugriff(Generator)
      

my_nums = square_numbers([1,2,3,4,5])  # hier wird mittels Generator zugegriffen, also flüchtige Daten.
#my_nums = [x*x for x in[1,2,3,4,5]]    # List Comprehension erzeugt eine neue Liste, die nicht flüchtig ist. WICHITG.

print (list(my_nums)) # wenn diese Liste gecastet wird, ist sie trotzdem nicht permanent. Das liegt am Generator.

# print (next(my_nums))
# print (next(my_nums))
# print (next(my_nums))
# print (next(my_nums))
# print (next(my_nums))  # ein neuer Eintrag würde zu einem Fehler führen(StopIteration), weil es keine weiteren Einträge in my_nums gibt.

# wenn mit next schon die Daten durchschritten wurden, können sie nicht mehr in der Schleife dargestellt werden,
# da sie nicht mehr im Speicher sind.

for n in my_nums:  # da der Generator nicht das gesamte Ergebnis im Speicher hält, muß man
                   # den Generator bzw. den yield Punkt immer wieder aufrufen.
    print(n)       # Der Generator bietet sich bei sehr großen Datenmengen an, die nicht auf einmal im Speicher gehalten werden können.


print(my_nums)   # hier kann nur ausgegeben werden, wenn eine List erstellt wurde. Ansonsten sind die Daten nicht im Speicher.