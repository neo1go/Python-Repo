import uuid
import csv
import os   # zum Löschen von Dateien 

class InventoryItem:
    def __init__(self, item_id, name, quantity, price):
        self.item_id = item_id
        self.name = name
        self.quantity = quantity
        self.price = price
        # uuid4 is the most universally used version. Die uuid wird also automatisch generiert.
        self.sku = str(uuid.uuid4())

    def display_info(self):
        print(
            f"Item ID: {self.item_id}, Name: {self.name}, Quantity: {self.quantity}, Price: {self.price:.2f}")


class InventoryManager:
    def __init__(self, file):  # Konstruktor
        self.file = file
        self.inventory = []    # List als Inventar
        self.next_item_id = 0
        
    def load_inventory(self):
        try:
            with open(self.file, "r") as file:  # hier wird nach der Nutzung die Verbindung sofort beendet und der GC ausgeführt durch 'with'.
                reader = csv.DictReader(file)
                self.inventory = [InventoryItem(
                            int(row["ItemID"]),
                            row["Name"],
                            int(row["Quantity"]),
                            float(row["Price"]),)
                                 for row in reader]
             #  self.next_item_id = len(self.inventory) + 1 #da immer erst die Datei geladen wird, wird die ID hier immer neu gesetzt. Kein guter Ansatz
                self.next_item_id = max((item.item_id for item in self.inventory), default=-1)+1
        except FileNotFoundError:
            print("No File...")
            

    def save_inventory(self):
        with open(self.file, "w", newline="") as file:
           fieldnames = ["ItemID","Name","Quantity","Price","SKU"]
           writer = csv.DictWriter(file, fieldnames=fieldnames)
           writer.writeheader()
           writer.writerows({
               "ItemID": item.item_id,
               "Name": item.name,
               "Quantity": item.quantity,
               "Price": item.price,
               "SKU": item.sku,
               }
                            for item in self.inventory)
           
           
           
    def add_item(self, name, quantity, price):
        item = InventoryItem(self.next_item_id, name, quantity, price)
        self.inventory.append(item)
        self.next_item_id += 1       # Zähler für ID erhöhen
        self.save_inventory()  # mit self wird sich hier auf das Objekt der Klasse bezogen. Sonst funktioniert die Methode nicht.
        
        
    def display_inventory(self):
        if not self.inventory:
            print("Empty inventory...")
        else:
            for item in self.inventory:
                item.display_info()
                
            
            
            
    def delete_item_by_id(self, item_id):
        self.inventory = [item for item in self.inventory if item.item_id != item_id]         # List Comprehension
        self.save_inventory()  # hier wird eigentlich eine komplett neue Liste erstellt minus der einen ID.
        # andere Variante 
        
        
    def filter_items(self, max_price):
        return [item for item in self.inventory if item.price <= max_price]

    
    def delete_file(self):
     if os.path.exists("inventory.csv"):
        os.remove("inventory.csv")
     else:
         print("The file does not exist")
       
       
    
    
def main():
    store = InventoryManager("inventory.csv")     # hier wird die Datei erstellt
    store.load_inventory()                        # grundsätzlich erstmal laden
    
    while True:
        print("\n===== E-Commerce System =====")
        print("1. Add an Item")
        print("2. Display Inventory")
        print("3. Filter items by price")
        print("4. Delete an item by ID")
        print("5. Save Inventory")
        print("6. Delete whole file")
        print("7. Exit")
        
        option = input("Enter your choice (1-6): ")
        
        if option == "1":
            name = input("Enter name: ")
            quantity = int(input("Enter amount of items: "))   #konvertiert sofort von string zu int etc.
            price = float(input("Enter a price: "))
            store.add_item(name, quantity, price)
            
            
        elif option == "2":
            store.display_inventory()
            
        elif option == "3":
            search = float(input("Enter a max price: "))
            filter_items = store.filter_items(search)
            print(f"Items less than {search}:")
            for item in filter_items:
                item.display_info()
            
            
            
        elif option == "4":
            id_num = int(input("Enter the ID of the item to delete: "))
            store.delete_item_by_id(id_num)
            print("Successfully deleted the item")
            
        elif option == "5":
            store.save_inventory()
            print("Saved to CSV") 
        
        elif option == "6":
            store.delete_file()
            
        elif option == "7":
            print("Good bye") 
            break
        else:
            print("Invalid option. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
