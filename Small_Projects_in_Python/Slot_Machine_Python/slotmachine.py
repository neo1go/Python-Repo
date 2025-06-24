# Slotmachine in Python

import random


def spin_row():
    symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']

    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("*************")
    print(" | ".join(row))
    print("*************")


def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
       match row[0]:
           case "🍒":
               return bet * 3
           case "🍉":
               return bet * 4
           case "🍋":
               return bet * 5
           case "🔔":
               return bet * 10
           case "⭐":
               return bet * 20
           case _:
               return 0
    
    return 0     # jede Methode in python gibt einen Wert zurück, Ist dieser nicht definiert, so wird "None" zurückgegeben. Das führt zu Problemen.
                 # Deswegen wird hier 0 zurückgegeben - der Daten-Typ ist hier entscheidend.
def main():
    balance = 100
    
    print("************************")
    print("Welcome to Pythons Slots")
    print("Symbols:🍒 🍉 🍋 🔔 ⭐")
    print("************************")
    
    while balance > 0:
        print(f"Current balance: €{balance}")
        
        bet = input("Place your bet amount: ")

        if not bet.isdigit():
            print("Please enter a valid number")
            continue
        
        bet = int(bet)
        
        if bet > balance:
            print("Insufficient funds")
            continue
        
        if bet <= 0:
            print("Bet must be greater than 0")
            continue 
            
        balance -= bet
        
        row = spin_row()
        print("Spinning....\n")
        print_row(row)
        
        payout = get_payout(row, bet)
        
        if payout > 0:
            print(f"You won €{payout}")
        else:
            print("Sorry you lost this round")
        
        balance += payout
        
        # play_again = input("do you want to play again? (Y/N)").upper()
        
        # if play_again != "Y":
        #     break

    print(f"\nGame over! Your final balance is €{balance}\n")



if __name__ == '__main__':
    main()
    

