def main():
    name = input("What's your name? ") 
    if not name:
        print(hello())
    else:
        print(hello(name))
    
    
def hello(to="World"):      # to ist hier ein default Wert. 
    return f"Hello, {to}"
    
    
if __name__ == "__main__":
    main() 