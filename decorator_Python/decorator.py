# Der decorator ist eine Funktion, die eine bestehende Funktion erweitert ohne die grundlegende Funktion zu ändern.
# Dabei wird die Basisfunktion als Argument dem Decorator übergeben.

def add_sprinkles(func):
    def wrapper(*args, **kwargs):       #der Wrapper ist notwendig, damit die innere Funktion nur dann ausgeführt wird, wenn die Basisfunktion get_ice_cream() aktiviert wird.
        print("*You add sprinkles 🎉*")
        func(*args, **kwargs)         # dies ruft die Basisfunktion auf, die übergeben wurde.  
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs): # Arguments und KeyWordArguments müssen übergeben werden vom wrapper an die func.
        print("*You add fudge 🍫*")
        func(*args, **kwargs)      # dies ruft die Basisfunktion auf, die übergeben wurde.
    return wrapper



@add_sprinkles 
@add_fudge    
def get_ice_cream(flavor):
    print(f"Here is your {flavor} ice cream 🍨")
    
get_ice_cream("vanilla")


