# nums = [1,2,3,4,5,6,7,8,9,10]

# my_list = []

# i want "n*n" for each "n" in nums
# alte Version
# for n in nums:
#     my_list.append(n*n)    
# print(my_list)

# result = [n*n for n in nums]   # dies ist list comprehension
# print(result)
# das geht auch mit map(). Map nimmt eine Kollektion und eine Funktion an und wendet die Funktion auf ALLE Werte der Collection an.

# Variante mit map. Die Map muss aber danach noch iterable gemacht werden.
# result = map(lambda n: n*n, nums)   # in diesem Fall ist die Funktion eine anonyme Lambda Methode und nicht eine vorher erstellte Methode.
# r = [r for r in result]  # es muß wie bei filter() nochmal extra iteriert werden weil vorher nur ein Iterator zurückgegeben wird, der ähnlich einem Generator ist.
# print(r)   

# Alte Variante
# i want 'n' for each 'n' in nums if 'n' is even
# for n in nums:
#     if n%2 == 0:
#         my_list.append(n)   
# print(my_list)

# Neue Variante mit filter und lambda . Filter nimmt wie Map auch eine Collection und eine Funktion, bearbeitet aber nur Werte, die der Bedingung entsprechen.
# my_list = filter(lambda n: n%2 == 0 , nums)  # es wird ein Iterator zurückgegeben der ähnlich einem Generator ist. Deswegen muß nochmal extra iteriert werden.
# result = [r for r in my_list]
# print(result)     #es geht auch ohne die result Schleife indem man typcastet als list.   print(list(result)) oder vorher die filter() Methode mit list wrappen.


# I want a (letter, num) pair for each letter in 'abcd' and each number in '0123'
# normale Variante mit nested loops
# for letter in "abcd":
#     for num in range(4):
#         my_list.append((letter, num))   
# print (my_list)

# neue Variante mit nested loops im Statement
# result = [(letter, num) for letter in 'abcd' for num in range(4)]
# print(result)

#---------------------------------------------------------------
# Dictionary Comprehension

# names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
# heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
# print(list(zip(names, heros, strict = False)))    # dies ist nur eine List

# ich will ein dict mit mit name, held für jedes Paar in zip 
# alte Variante
# my_dict = {}
# for name, hero in zip(names, heros):
#     my_dict[name] = hero
# print(my_dict)   # jetzt ist es ein dict

# neue kurze Variante, dict-comprehension
# my_dict = {name: hero for name, hero in zip(names, heros)}
# print(my_dict)

# das gleiche nochmal aber mit einer Bedingung (condintional) ähnlich einem Filter.
# my_dict = {name: hero for name, hero in zip(names, heros) if name != 'Peter'}
# print(my_dict)

#---------------------------------------------------------------
# Set Comprehension 

nums = [1,1,2,1,3,4,3,4,5,5,6,7,8,7,9,9]
# alte Variante
# my_set = set()
# for n in nums:
#     my_set.add(n)  # Duplicates will be ignored.
# print(my_set)

# Set-Comprehension ,also neue Variante
# my_set = {n for n in nums}
# print(my_set)

#---------------------------------------------------------------
# Generator Expression
# ein Generator hält nur immer einen Wert zu einer Zeit im Speicher (vorhalten des Wertes -> yield) und muß dann mittels einer nichtsichtbaren next Methode weiter iterieren.

# I want to yield 'n*n' for each 'n' in nums
# def gen_func(nums):
#     for n in nums:
#         yield n*n

# my_gen = gen_func(nums)    # my_gen hat hier immer nur einen Wert gespeichert.

# for i in my_gen:   # implizites Aufrufen von next()
#     print(i)
    
    
# Generator Expression
my_gen = (n*n for n in nums)    #nur wegen der runden Klammern. Wären sie eckig, dann wäre es kein Generator und wir bräuchten keine Schleife.
for i in my_gen:   # hier wird imlpizit next() aufgerufen
    print(i) 
