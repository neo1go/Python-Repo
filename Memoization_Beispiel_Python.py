from functools import wraps
from time import perf_counter
import sys


# die rekursive Natur läuft hier so ab:
# Alle Schritte werden von der n Zahl aus zerlegt und erst wenn die Aufrufe bei
# der Durchdringung am basecase angelangt sind,
# werden bei dem Rücklauf nach "oben" die richtigen fibonacci return Werte
# addiert.
# Es wird also quasi ein Binärbaum mit Funktionsaufrufen erstellt und beim
# Erreichen des Basecase wird alles returned,
# weil dann ja kein neuer Aufruf mehr stattfindet.

# Mittels des Wrappers memoize() wird hier eine bessere Performance erreicht, da das dict
# die schon berechneten Werte speichert,
# die durch die binäre Struktur des rekursiven Aufrufs immer wieder auftreten
# können.


def memoize(func):  
    cache = {}     # hier werden die n Funktionsaufrufe als key gespeichert.

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)
        
        if key not in cache:
            cache[key] = func(*args, **kwargs)
            
        return cache[key]
        
    return wrapper

@memoize      # hier wird eigentlich das gemacht:  fibonacci = memoize(fibonacci) <-das ist der Wrapper
def fibonacci(n) -> int:
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)  # das ist divide and conquer 

if __name__ == "__main__":
    sys.setrecursionlimit(10_000)    # Systemzugriff  ACHTUNG UNSAFE
    start = perf_counter()         # speziell zur Messung 
    f = fibonacci(8)
    end = perf_counter()
    
    print(f)
    print(f'Time: {end - start} seconds Duration of the calculation')