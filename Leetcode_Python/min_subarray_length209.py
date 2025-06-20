# Leetcode 209 Minimum Size Subarray Sum
# Ziel ist die Rückgabe der kürzesten zusammenhängenden Summen-Gruppe
# also bei 2,3,1,2,4,3 und dem target 7 ist die Antwort 2 für die Werte 4 und 3
# kann die Summe nicht erreicht werden, wird 0 zurückgegeben.
# der linke Pointer wird nachgezogen und der rechte Pointer iteriert einfach weiter.

class Solution(object):
    def min_subarray_len(self, target, nums):
        left = 0 # obwohl es eine 2 Pointer Lösung ist, wird nur ein linker eigenständiger Pointer benötigt.
        current_sum = 0
        min_length = len(nums)
        if sum(nums) < target:
            return 0

        for right in range(len(nums)):   # dies ist der rechte Pointer 
            current_sum += nums[right] # Den aktuellen Wert addieren
            
            while current_sum >= target:
                min_length = min(min_length, right - left + 1)
                current_sum  -= nums[left]  # linken Wert subtrahieren da ja die Summe größer oder gleich dem target ist laut der while Bedingung.
                left += 1 # linken Pointer um eins nach rechts versetzen.
        return min_length
     

nums = [2,3,1,2,4,3]
target = 7
solution = Solution()

print(f"Die kürzeste Strecke ist: {solution.min_subarray_len(target, nums)}")