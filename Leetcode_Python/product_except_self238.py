# Leetcode 238
# meine Lösung ist: von nums den ersten Wert aus dem Array löschen,
# dann jeden Wert mutliplizieren und anschliessend den ersten Wert hinten wieder 
# anfügen. Die Schleife läuft für die Länge des Arrays, also range(len(nums))
# Meine Lösung funktioniert nur bei kleinen nums Arrays weil es sonst einen
# Laufzeitfehler gibt.
# Die effizienteste Lösung arbeitet mit 2 Produkten, nämlich Links und Rechts vom
# aktuellen Wert. Diese Produkte werden in 2 Arrays eingetragen und dann an der Indexstelle multipliziert.
#
# für 1,2,3,4
# Links  = [_    ,   1, 1*2, 1*2*3]    die underscores werden später mit 1 initialisiert
# Rechts = [2*3*4, 3*4,   4,     _]

# jetzt an jedem Index Links mit Rechts multiplizieren und in result eintragen.
# result = [24   ,  12,   8,     6]

# die Produkte des linken und rechten Arrays für sich sind kleiner als ein gesamtes Produkt
# und somit können grössere Werte verarbeitet werden.


class Solution(object):    
    """
    # Brute Force mit 2 Schleifen
    def productExceptSelf(self, nums):
        result = []  
        n = len(nums)
        
        for i in range(n):
            value = 1    # wird nach jedem Durchlauf wieder auf 1 gesetzt
            for j in range(n):
                if i != j:   # hiermit wird der aktuelle Wert immer ommited
                    value *= nums[j]
            result.append(value)
        return result
        """
    def productExceptSelf(self, nums):
        n = len(nums)
        left = [1] * n    # alles wird mit 1 und der Länge von nums initialisiert.
        right = [1] * n
        # result = [0] * n  # geht auch mit append
        
        # hier wird Index 0 ignoriert und hat noch Wert 1 wie gewünscht
        for i in range(1, n):  # alle Werte links von i werden multipliziert
            left[i] = left[i-1] * nums[i-1] # hier wird immer kaskadenartig der aktuelle Wert mit dem vorherigen Produkt multipliziert. (dynamic programming)
            #aktuelle Stelle = vorherige Stelle * Wert im nums Array an i-1 weil nur Werte links von i genommen werden sollen zur Multiplikation.
            
            
            #   Ende des Arrays, -1 ist nicht inkludiert also bis 0, Schrittweite ist -1
        for i in range(n - 2, -1, -1):  # -2 weil der letzte Wert im rechten Array auf 1 stehen bleiben soll.
            right[i] = right[i+1] * nums[i+1] # right[i+1] ist das Produkt der vorherigen Berechnung und nums[i+1] muß man machen da bei Index 0 ja nur rechte Werte in Frage kommen.
        
        
        # for i in range(len(nums)):
        #     result[i]= left[i] * right[i]
        
          
          # weitere Variante
        result = []
          
        # for i in range(n):
        #     result.append(left[i] * right[i])
        
        # weitere Variante   
        result = [left[i] * right[i] for i in range(n)]
         
        return result
        
              
nums = [1,2,3,4]
# nums = [3,4,6,1,2]
# nums = [-1, 1, 0, -3, 3]
result = Solution().productExceptSelf(nums)

print(result)