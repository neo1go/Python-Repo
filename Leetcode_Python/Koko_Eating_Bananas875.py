# Coco eating banana Leetcode Nr. 875
# Der Affe soll eine bestimmte Menge Bananen essen in einer bestimmten Zeit h und kann immer nur einen
# Haufen (ein Zahlenwert) pro Stunde essen, also keine Überschneidungen.
# Der Affe soll so langsam wie möglich essen.

# Bspl.:
# [3,6,7,11] h=8       Antwort ist 4 Bananen pro Stunde
#  1Std,2Std,2Std,3Std = 8 Std
#  (1x4,2x4,2x4,3x4)
import math


class Solution(object):
    def minEatingSpeed(self, piles, h):
        # basecase early return
        if len(piles) == h:
            return max(piles)
        
        left = 1
        right = max(piles)
        result = right # worst case ist der Maximalwert
        
        # binary search
        while left <= right:
            mid = (left + right) // 2
            total_hours = 0
            
            for pile in piles:
                total_hours += math.ceil(pile / float(mid)) # jeder einzele Teilwert wird abgerundet und dann addiert, das ergibt die Stunden je Eintrag.

            if total_hours <= h: 
                result = mid
                right = mid - 1
                
            else:
                left = mid + 1
            
        return result
             
      
piles = [30,11,23,4,20]    
#piles = [3,6,7,11]  # h = 8
h = 6

print(Solution().minEatingSpeed(piles, h))