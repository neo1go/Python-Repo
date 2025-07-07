# um Listen zu erweitern, gibt es zwei Möglichkeiten,
# 1. append, das aber nicht einzeln iteriert über den angehangenen Datensatz
# 2. extend, welches auch über den angehangenen Datensatz iteriert. Dadurch kann man sich das Loopen über einen Datensatz mit append im Loopbody sparen.
# Bslp.:


import timeit
from typing import Any, Iterable
# Anstatt:    
def append(alist: list[Any], iterable: Iterable[any]) -> None:
     for item in iterable:
         alist.append(item)

# kann man schreiben:
def extend(alist: list[Any], iterable: Iterable[any]) -> None:
    alist.extend(iterable) 
#Die extend Methode ist wesentlich performanter.

print('Running benchmarks...')
print('Append:', min(timeit.repeat(lambda: append([],'a'*200))))
print('Extend:', min(timeit.repeat(lambda: extend([],'a'*200))))

#------------------------------------------
l1: list[str] = ['a','b']
l2: list[str] = ['a','b']

#l1.append(['c','d'])  # fügt ein Element in Form einer List an. Man kann nicht gleichzeitig mehrere Listen anfügen.
l1.append('bob')
l2.extend('bob')  # es wird einzeln über die chars iteriert. Das ist die Besonderheit von extend. Es sollte speziell zum Iteriern genutzt werden.

print(l1)
print(l2)

l3: list[str] = []
l4: list[str] = []
print('-----------------')

print(f'{id(l3)=}')
l3 = l3 + ['1','2']  # WICHTIG: erzeugt eine komplett neue List l3. Es wird nicht konkateniert.
print(l3) 
print(f'{id(l3)=}')  # hier ist die Speicheradresse eine andere. Die List wurde komplett neu erstellt(neues Objekt).
print('-----------------')
print(f'{id(l4)=}')
l4 += ['1','2']
print(l4)  # hier wird am bestehenden Speicherplatz der String um die chars erweitert(in place).
print(f'{id(l4)=}')  # hier ist die Speicheradresse die gleiche da die Werte nur angehangen werden an den bestehenden Datensatz.
