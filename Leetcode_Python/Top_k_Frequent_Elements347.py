# Leetcode 347 Top k Frequent Elements 
# Es sollen die Zahlen mit den häufigsten Aufkommen zurückgegeben werden.
# Dabei wird die Anzahl des Resultatswerte durch die Häufigkeit k begrenzt.
# Es sind also verschiedene Antworten zulässig.
# Bspl.:
# [1,1,1,2,2,2,3,3,3,4,5,6,7,7,7] und k = 3 -> 1,2,3 oder 2,3,7 oder 1,2,7 aber nicht 1,2,3,7

class Solution(object):
    def topKFrequent(self, nums, k):
        amount = {}
        result = []
        
        # Erstellung der Dict-Häufigkeitsliste,also das Aufkommen einer bestimmten Zahl
        for num in nums:
            amount[num] = amount.get(num, 0) + 1 # wenn Wert exisitert, wird er um 1 erhöht oder gesetzt -> Kurzschreibweise
        
        print(f"Anzahl(Zahl/Aufkommen): {amount}")
        
        # Durch max wird der Längenwert des neu zu erstellenden Dicts ermittelt.
        highestVal = max(amount.values())
        
        # Buckets-Dict wird erstellt. Jeder bucket enhält nun erst den Key für die jeweilige Zahl 
        buckets = {i: [] for i in range(1, highestVal + 1)}
        
        # Hier werden die Values für die Buckets eingetragen, es wird ein dict mit leeren Stellen, wenn die Zahl nicht 
        # vorkam. Also z.B. [1,1,3] ->Zahl/Aufkommen {1:2,2:0,3:1}-> jetzt wird es rumgedreht quasi -> {0:1,1:1,2:1} -> es wird [1,2] ausgegeben.
        for num, freq in amount.items():
            buckets[freq].append(num) # hier werden nun die Werte gesetzt, basierend auf den ursprünglichen Keys des anderen Dict.
        
        print(f"Buckets (Anzahl/Zahl): {buckets}")
        
        # Hiermit wird die Result-List befüllt, bis k erreicht ist.
        for freq in reversed(range(1, highestVal + 1)):
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result # u.U. early return, es können Werte abgeschnitten werden.
        
#nums = [1,2,3,3,4,4]
#nums = [1,1,3]
nums = [1,1,1,2,2,2,3,3,3,4,5,6,7,7,7] # hier wäre logischerweise eigentlich 1,2,3,7 die Antwort. Leetcode will aber 
# die top k Elemente, egal welche -> [1,2,3] oder [2,3,7] oder [1,3,7] aber NICHT [1,2,3,7]
k = 3

print(Solution().topKFrequent(nums, k))