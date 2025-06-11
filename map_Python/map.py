# map(function, collection) wendet eine bereitgestellte Funktion auf alle Elemente einer Collection an.


def c_to_f(temp):
    return (temp * 9/5) + 32

celsius_temps = [0.0, 15.0, 25.0, 40.0, 44.0, 18.0]

# normale Variante
# fahrenheit_temps = map(c_to_f, celsius_temps)

# for temp in fahrenheit_temps: 
#    print(temp)
   
      
# kurze Variante
fahrenheit_temps =list(map(c_to_f, celsius_temps))  # typecasting zu einer List. Hier wird eine Funktion übergeben 
print(fahrenheit_temps)


# lambda Variante mit anonymer Funktion
lambda_temps = list(map(lambda temp: (temp * 9/5) + 32, celsius_temps))  # hier wird die Lambda Funktion genutzt, also eine anonyme Funktion
print(lambda_temps)

