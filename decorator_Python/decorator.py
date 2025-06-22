# Der decorator ist eine Funktion, die eine bestehende Funktion erweitert ohne die grundlegende Funktion zu ändern.
# Dabei wird die Basisfunktion als Argument dem Decorator übergeben.

# *args sind eine beliebige Anzahl an Positionsargumenten
# **kwargs sind eine beliebige Anzahl an Schlüsselwortargumenten



def add_sprinkles(func):
    def wrapper(*args, **kwargs):       #der Wrapper ist notwendig, damit die innere Funktion nur dann ausgeführt wird, wenn die Basisfunktion get_ice_cream() aktiviert wird.
        print("*You add sprinkles 🎉*")
        func(*args, **kwargs)  # dies ruft die Basisfunktion auf, die übergeben wurde. Die wildcards * u. ** gewährleisten die größtmögliche Flexibilität bei der Übergabe.  
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs): # Arguments und KeyWordArguments müssen übergeben werden vom wrapper an die func.
        print("*You add fudge 🍫*")
        func(*args, **kwargs)      # dies ruft die Basisfunktion auf, die übergeben wurde. Die wildcards * u. ** gewährleisten die größtmögliche Flexibilität bei der Übergabe. 
    return wrapper



@add_sprinkles   # im stack frame an erster Stelle 
@add_fudge    
def get_ice_cream(flavor):
    print(f"Here is your {flavor} ice cream 🍨")
    
 # ACHTUNG -> get_ice_cream wird von add_fudge ummantelt und diese beiden werden dann von add_sprinkles ummantelt. Dies geschieht beim Laden des Codes(von unten nach oben)
 # Beim Ausführen wird dann der äußere Wrapper add_sprinkles zuerst ausgeführt, gefolgt von add_fudge und zuletzt get_ice_cream, wie eine Zwiebel von außen nach innen.
    
 # Erstellung des Wrapp Objektes   
 # - fudge umhüllt get_ice_cream , indem es die func annimmt und mittels def wrapper umhüllt.
 # - dann umschließt add_sprinkles dieses schon gewrappte Objekt nochmals, indem es die func fudge mit dem gewrappten get_ice_cream entgegennimmt und mit def wrapper wrappt.

 # Ablauf des Aufrufs
 # es wird "get_ice_cream" aufgerufen, was in Wirklichkeit die äußere Wrapperfunktion, also "add_sprinkles", aufruft.
 # "add_sprinkles" führt die eigene Logik aus und ruft dadurch die gewrappte Funktion "add_fudge" auf.
 # "add_fudge" führt dann seine Logik aus und gibt damit die von ihm gewrappte Funktion "get_ice_cream" zurück.


# auch wenn hier get_ice_cream steht, so ist dies außen mit add_sprinkles() gewrappt und add_sprinkles() steht auch im stack-frame an erster Stelle.
get_ice_cream("vanilla") 


