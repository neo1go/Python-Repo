# reduce wird genutzt, um eine Funktion auf ein Iterable anzuwenden um dieses auf einen zusammengefassten Wert zu reduzieren.
# Es werden in reduce immer die ersten zwei Werte miteinander kombiniert bis nur noch ein zusammengefasster Wert übrig bleibt.

# reduce(function, iterable)

import functools



letters = ["H","E","L","L","O"] # H+E, HE+L, HEL+L, HELL+O

word = functools.reduce(lambda x, y :x + y, letters)
print(word) 

factorial = [5,4,3,2,1]
result = functools.reduce(lambda x, y : x * y, factorial)
print(result)