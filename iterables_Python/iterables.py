# Ein Objekt oder eine Collection, die ein Element zu einer Zeit zurückgeben kann 
# und mittels eines loops durchschritten wird, ist iterable, also "durchschreitbar".

# iterables sind list, tuple, dictionary, string


#++++++++String++++++++++
name = "Gordon H"

for char in name:
    print(char, end="")

print("\n")


#+++++++++List+++++++++++
numbers = [1, 2, 3, 4, 5]

for number in reversed(numbers):
    print(number, end=" - ")
    
print("")


#+++++++++Tuple++++++++++
tuple_numbers = (1,2,3,4,5)  # Tuple stehen fest und können nur erweitert aber nicht verändert werden.

for tuple in tuple_numbers:
    print(tuple)
    
print("")



#+++++++++Set++++++++++++

set_of_numbers = {1, 1, 2, 2, 3, 4, 5, 5}  # Duplikate werden nicht erfasst.

for unique_value in set_of_numbers:
    print(unique_value)
    
  
    
#+++++++Dictionary++++++++

my_dictionary = {"Banana": 15, "Apple": 5, "Carrots": 10}

for key in my_dictionary:
    print(key)
    
for value in my_dictionary.values():     # mit .values() lassen sich die Werte anzeigen.
    print(value)
    
for key, value in sorted(my_dictionary.items(),key= lambda item: item[1], reverse=True):
    print(f"Key = {key}, Value = {value}")