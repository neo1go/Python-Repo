# Leetcode 33
# Zahl in einem rotated Array suchen.
# Wird der Wert nicht gefunden, returned man -1
# Es gibt eine Brute Force Variante, die alle Zahlen durchläuft und sehr ineffizient ist.
# Die andere Möglichkeit ist binary search.
# Der einzige Unterschied ist, das der Übergang mit behandelt werden muß.
#  
# z.B.
# [2,3,4,0,1] target = 0   man landet beim ersten Halbieren auf 4, was größer ist und muß 
# eigentlich nur in Erfahrung bringen, ob alles ascending ist(left<mid<right). 
# Ansonsten wird der linke oder, je nachdem, der rechte Pointer gegenteilig gesetzt zur üblichen Vorgehensweise.


class Solution(object):
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        mid = (left + right) //2

        while left <= right:               # Pointer laufen aufeinander zu
            mid = (left + right) // 2      # muß immer neu berechnet werden
            
            if nums[mid] == target: # early return
                return mid
                
            # linke Hälfte    
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]: # bei normaler Verteilung wird der Pointer auch wi üblich nach links verschoben
                    right = mid - 1
                else: #diese Else Bedingung trifft dann ein, wenn ein Übergang gefunden wurde.
                    left = mid + 1 
                    
            # rechte Hälfte        
            elif nums[right] >= nums[mid]: 
                if nums[mid] < target <= nums[right]: # wenn ascending order
                    left = mid + 1
                else:#diese Else Bedingung trifft dann ein, wenn ein Übergang gefunden wurde.
                    right = mid - 1 
                    
        return -1
        
        
nums = [4,5,6,7,0,1,2]
target = 0

print(Solution().search(nums, target))