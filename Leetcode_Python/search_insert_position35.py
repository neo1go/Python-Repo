# Leetcode 35
# Search insert position
# Es wird zuerst klassisch mit binary search der Wert gesucht und , falls vorhanden, returned.
#
# Der Trick der ganzen Aufgabe besteht hierin:
# Der linke Pointer steht immer an der Stelle, an der der Wert eingefügt werden muß. Das ergibt sich aus dem binary search.
#
# Bspl.:
# [1, 3, 4, 6] target = 5
# erster Durchlauf
# Indexe left = 0  right = 3 und mid =1 also ist target größer als nums[mid]
# zeiter Durchlauf
# target ist größer als Value 4 , also left mid +1, also Index 3
# dritter Durchlauf
# target ist kleiner als Value 6, also right = 2 und Ende des binary search. left = 3 und right = 2
# Somit steht left genau an der Stelle, an der 5 eingefügt werden kann.


class Solution(object):
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums)-1
               
        # binary search
        while left <= right:
             mid = (left + right) //2              
             if nums[mid] == target:
                 return mid                   
             elif nums[mid] > target:
                 right = mid - 1 
             else:
                 left = mid + 1
        return left    
       
nums = [1,3,5,6]
target = 5
sol = Solution()

print(sol.searchInsert(nums, target))