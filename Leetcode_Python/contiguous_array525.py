# Achtung -> die -1 wird in dieser Aufgabe quasi für fast 3 unterschiedliche Funktionalitäten genutzt:
# als Startindex, um bei -1 neutral anzufangen
# als Austausch für alle Nullen im  gegebenen Array was dann dazu führt dass ->
# man die -1 und +1 für die Balancerechnung herranzieht um einen Graphen und dessen Plus oder Minuswerte zu simulieren.


def contiguous_array(nums):
    new_nums = [-1 if c == 0 else 1 for c in nums] # damit werden alle 0 zu -1
    hash_map ={0:-1}   # Key 0 an Startindex -1,. Das ist verwirrend da die -1 nicht die current_sum zum Ausgleichen darstellt sondern einfach den technischen Startwert 
    # für das Array. WEnn also eine ausbalancierte Sequenz am Anfang beginnt, dann kann mit -1 direkt die korrekte Länge berrechnet werden.
    current_sum = 0 # dies ist der Key, an dessen mehrmaligem versuchten Eintragen in das dict(stellvertretend für den Graphen), dann die maximale Länge ermittelt werden kann. 
    # Also immer, wenn ein Key schon vorhanden ist im dict, misst man (Das ist das Auftauchen des gleichen Wertes im Graphen, egal ob im Plus oder Minus Bereich) 
    # vom aktuellen Index bis zum ersten Index mit dem selben Wert die Länge.
    max_length = 0 # die maximale Gesamtlänge für die List


    for i in range(len(new_nums)):
        current_sum += new_nums[i] # hier passiert die wichtige Addition oder Subtraktion im Falle von -1. Dies entspricht dem Auf und Ab in einem Graphen
        if current_sum in hash_map: # wenn key schon in hashmap vorhanden ist, dann:
            prev_index = hash_map[current_sum] # das ist der Index des erstmaligen Auftauchens des Wertes im Dict, so easy.
            max_length = max(max_length, i - prev_index)# bererechnet die Maximallänge anhand des Index des ersten Auftauchens im dict mit dem aktuellen Index
        else:
            hash_map[current_sum] = i 
    return max_length

   

nums1 = [0,0,0,0,1,1]# dies entspricht [-1,-1,-1,-1,0,0]
# was nun passiert ist: (für nums1)
#  Durchlauf   Wert an der Stelle   Summe (die -1 ist einfach der Startindex) Die Summe ist der einzigartige key
#    -1                               0
#     0            -1                -1
#     1            -1                -2
#     2            -1                -3
#     3            -1                -4
#     4             1                -3   Länge ist 2 von der vorherigne -3 zu dieser -3(die ja in Wirklichkeit nicht eingetragen wird da sie schon mal vorgekommen ist.)
#     5             1                -2   die Summen und deren erneutes Auftauchen werden stetig verglichen
#                                         und die -2 war schonmal an Index 1, also Index 5 minus Index 1 gleich Ergebnis Maximallänge 4.
# dabei wird also das schonmalige Auftauchen eines Wertes verglichen. 
nums2 = [0,0,1,0,0,0,1,1]

print (f"Dier Länge beträgt {contiguous_array(nums1)}")
