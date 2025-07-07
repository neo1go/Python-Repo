def get_string_methods():
    i: int = 0
    for method in dir(str):  # dir(str) zeigt alle Attribute inklusive Methoden der Klasse string an.
        if '__' not in method:   # dunder Methoden werden ignoriert.
            i += 1
            print(i, method, sep=': ')    #sep ist der Teiler zwischen i und dem Methodenbezeichner
            
            
get_string_methods()


# 1: capitialize()    # macht nur den ersten Buchstaben groß
text1: str = 'HELLO'
print(text1.capitalize())   

# 2: casefold()   # wird genutzt, um strings ungeachtet ihrer Groß oder Kleinschreibung gleich zu behandeln.
text2: str = 'MARIo'
text2_1: str = 'mariO'
print(text2.casefold())
print(text2_1.casefold())

# 3: center()  # zentriert den String in der Mitte und setzt bei Bedarf einen bestimmten char zu Auffüllen bis zur gewünschten Stringlänge. Der Ursprungsstring ist inklusive.
text3: str = 'Luigi'
print(text3.center(20, '.'))    # 20 Zeichen ist die Gesamtlänge inklusive dem String.

# 4: count()   # zählt die Anzahl an Substrings 
text4: str = 'abc_abc_abc_abc'
print(text4.count('ab'))

# 5: encode()  # gibt die binäre Repräsentation eines Strings zurück. Die Option strict gibt an, das bei einem Fehler ein Error geworfen wird.
text5: str = 'Elon Musk'
print(text5.encode(encoding='UTF-8', errors='strict'))

# 6: endswith()    # vergleicht den Char oder String mit dem Ende des zu vergleichenden Strings und gibt einen bool zurück.
text6: str = 'apple'
print(text6.endswith(('z','e'))) # bei nur einem '' Paar reicht eine Umklammerung(), bei mehreren '' Paaren muß noch ein () Klammerpaar hinzugefügt werden.
                    # dies ist eine OR Abfrage zwischen z und e.

# 7: expandtabs()   # erweitert jeden TAB um einen Wert an Leerzeichen
text7: str = 'text\ttext2\ttext3'      # \t sind tabs 
print(text7.expandtabs(20))

# 8: find()
text8: str = 'Remember to fart in the wind!'
position: int = text8.find('fart')  # wenn der Substring nicht gefunden wird , wird -1 returned, ansonsten der Startindex im String(ab 0 zählen)
print(position)
print(text8[position:16])   # hier werden alle chars ab der gefundenen Position bis zum Ende des Wortes angezeigt. Wird die Zahl weggelassen, wird der gesamte Rest des Strings mit angezeigt.

#9: format()
text9: str = '{subject} is doing: {action}.'
print(text9.format(subject='Cat', action='meow'))

text9_2: str = '{} is doing: {}.'  # Alternative
print(text9_2.format('Cat', 'meow'))

#10: format_map()
coordinates: dict = {'x': 10, 'y': -5}
text10: str = 'Coordinates: ({x}, {y})'  # es werden die Values der dict-Keys übergeben
print(text10.format_map(coordinates))

#11: index()     # im Gegensatz zu find() wird hier beim Nichtfinden des chars oder strings ein Error geworfen.
text11: str = 'Astronauts recently discovered a banana on the moon?'
position_1: int = text11.index('banana')
print(position_1)
print(text11[position_1:])   # es werden ab dem Finden des Wortes alle danach folgenden chars angezeigt.  

#12: isalnum()    # is alphanumeric? Wenn also andere Zeichen als Buchstaben oder Zahlen im String vorhanden sind wie z.B. Klammern oder andere Sonderzeichen,
                  # dann wird ein False zurückgegeben.
text12: str = 'hellokitty123()'
print(text12.isalnum()) 

#13: isalpha()  # also nur alphabetic (nur Buchstaben)
text13: str = 'helloKitty123'
print(text13.isalpha())

#14: isascci()
text14: str = 'Hello©️'   # das c ist kein ASCII und somit wird false ausgegeben.
print(text14.isascii())

#15: isdecimal()   # nur für Dezimalzahlen des arabischen Nummernsystems
text15: str = '123'
print(text15.isdecimal())

#16: isdigit()    # gibt true zurück, auch wenn das Zeichen nicht dezimal ist wie z.B. eine eingekreiste 5. Funktioniert mit isdigit() und isdecimal() Werten.
text16: str = '\u2464'  # eingekreiste 5
#print(text16)
print(text16.isdigit())

#17: isnumeric()     # funktioniert mit isnumeric(), isdigit() und isdecimal() Werten. Gilt also für alle 4 Varianten
text17: str = '߁'   # eine 1 in einer anderen Sprache gilt auch als numerisch, ist aber nicht arabisch.
print(text17.isnumeric())

#18: isidentifier()   # stellt fest, ob ein string ein valider Variablenname sein kann.
text18: str = 'test-sample'   # der Bindestrich ist nicht erlaubt für Variablen in python.
print(text18.isidentifier())

#19: islower()    # vergleicht, ob alle chars im string klein geschrieben sind.
text19: str = 'Abc'  
print(text19.islower())

#20: isprintable()     # hiermit kann man auch Eingaben überprüfen und unzulässige Zeichen unterbinden wie z.B. \n \t , ANSI Farben oder ASCII Steuerzeichen.
text20: str = 'text\n'   # gibt ein false weil escape sequences nicht sichtbar sind. Das heißt, das nicht der ganze String anzeigbar wäre.
print(text20.isprintable())

#21: isspace()  # kontrolliert, ob nur spaces im string sind und keine anderen Zeichen
text21: str = '     '
print(text21.isspace())

#22: istitle()
text22: str = 'Hello New Video here'
print(text22.istitle())    # checkt, ob ein String in dem Title Format geschrieben wurde, das heißt Großbuchtaben bei jedem neuen Wort.

#23: isupper()      # vergleicht, ob alle chars im string groß geschrieben sind.
text23: str = 'BANANAS'
print(text23.isupper())

#24: join()
text24: str = '-'
print(text24.join(['text1', 'text2', 'text3']))
# geht auch ohne Variable
print('-'.join(['neuerText1', 'neuerText2', 'neuerText3']))

#25: ljust()   left adjustment, soweit wie möglich nach links verschieben und rechts eine Anzahl an Zeichen anhängen
text25: str = 'text'
print(text25.ljust(20, '_'))

#26: lower()   # im Gegensatz zu islower wird hiermit ein String komplett umgewandelt in Kleinbuchstaben.
text26: str = 'UPPERCASE LETTERS'
print(text26.lower())

#27: lstrip()    # Entfernt strings oder chars von der linken Seite des Strings.
text27: str = 'Some text.'
print(text27.lstrip('Some '))

#28 & 29: maketrans() & translate() 
text28: str = 'That is a Big Bacon Burger.'
table = text28.maketrans('B', '😁')    # alle B's werden umgewandelt. {66: 128513}  66 ist B in Unicode.

print(table)   #Übersetzungstabelle, die für sich alleine noch nicht nutzbar ist.
print(text28.translate(table))

#30 partition()
text29: str = 'a+b=c'
print(text29.partition('='))   # es wird der String in drei Bereiche aufgeteilt und das Gleichheitszeichen ist das Trennzeichen zwischen den beiden Seiten.

#31 removeprefix()
text30: str = 'Wazzap'
print(text30.removeprefix('Waz'))

#32 removesuffix()
text31: str = 'Mister Everyone'
print(text31.removesuffix('one'))

#33
