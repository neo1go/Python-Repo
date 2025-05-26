def main():
    name = input("What's your name? ")
    print(hello(name))
    
    
def hello(to="world"):  # to ist hier ein default Wert. 
    return f"hello, {to}"
    
    
if __name__ == "__main__":
    main()