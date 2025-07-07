from uuid import uuid4
# Um bei der Nutzung von id in der Subklasse nicht die erste ID überschreiben zu lassen bzw sie doppelt zu belegen, wird name_mangling genutzt.
# Das bedeutet, das die Variable in der Superklasse private gesetzt wird. Dadurch wird bei Account eine andere ID als bei SavingsAccount erstellt.
# Man kann auch die Variable der Subklasse private setzen. Dies verhindert auch die Doppelbelegung.

class Account:
    def __init__(self, name: str) -> None:
        self.name = name
        self.__id = f'ACCOUNT: {uuid4()}' 
           
    def show_account_id(self) -> None:
        print(self.__id)
 
 
# Subklasse 
class SavingsAccount(Account):
    def __init__(self, name: str) -> None:
        super().__init__(name)           #der Konstruktor der Superklasse wird genutzt       
        self.__id = f'SAVINGS: {uuid4()}'
        
    def show_savings_id(self) -> None:
        print(self.__id)   
        
        
        
def main() -> None:
    # acc: Account = Account("Savings")
    # acc.show_account_id()
    # print(acc._Account__id)  # besondere Schreibweise, mit der man trotzdem auf eine private Variable zugreifen kann.
    
    savings: SavingsAccount = SavingsAccount("Bob's savings")
    savings.show_account_id() # wenn nicht id oben in der Superklasse auf private gesetzt wird, zeigen diese beiden Methoden die gleiche ID an.
    savings.show_savings_id()
    
    

if __name__ == '__main__':
    main()

