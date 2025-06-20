class Solution(object):
    def divide(self, dividend, divisor):
        INT_MAX = 2**31 - 1 
        INT_MIN = -abs(2**31)
        # Sonderfall, der einen Overflow verhindert 
        if dividend == INT_MAX and divisor == -1:
            return -abs(INT_MAX)
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        if divisor == 0:
            return "not working"
        
        if dividend == 0:
            return 0
              
        result = 0
        
        negative = (dividend < 0) != (divisor < 0)  # setzt einen bool auf negativ,  wenn eines der beiden Vorzeichen negativ ist
        dividend = abs(dividend)  # Zähler
        divisor = abs(divisor)    # Nenner

        # Effiziente Division durch Bit-Shifting. Der Dividend wird immer weiter verkleinert durch das Abziehen der multiplen divisor Werte
        # die BESONDERHEIT dieser bit Berarbeitung:
        # es wird der divisor Wert andauernd verdoppelt , quasi wie beim binary search, nur anders angewandt.
        # Somit muss man auch den Zähler "multiple" parallel mit verdoppeln.
        # Kann man dann nicht mehr verdoppeln, z.B. wegen ungeraden Teilern, wird, da ja immer wieder 
        # temp und multiple auf den Grundwert zurückgesetzt werden, einmal subtrahiert vom Dividend bzw
        # nur einmal aufs result addiert. 16/5 = 10,also 2x, der Rest ist 6/5 = 1. Diese 1 wird dann noch zu
        # zu dem 2x hinzuaddiert und das Ergebnis ist 3. Es wird auch nicht weitergerechnet, da ja der Dividend 1 kleiner als 5 ist.
        
        while dividend >= divisor:
            temp = divisor # temp wird nach der inneren Schleife wieder auf den Ursprungswert gesetzt
            multiple = 1 # Reset auf Ursprungswert
            while dividend >= (temp << 1):
                temp <<= 1  # dies ist eine Verdoppelung des temp Wertes
                multiple <<= 1 # diese ist  multiple *=2, aber bitweise
            dividend -= temp   # diese beiden Vorgänge sind immer nach der inneren While Schleife.
            result += multiple

        return -result if negative else result # basierend auf der Flag des bools 'negative'.
        
        



print(f"Wie oft vorhanden {Solution().divide(10,3)}")
print(f"Wie oft vorhanden {Solution().divide(10,-3)}")
print(f"Wie oft vorhanden {Solution().divide(-2147483648,-1)}")

# es würde auch gehen:
sol = Solution()  # Klasseninstanz
print(sol.divide(10,4))  