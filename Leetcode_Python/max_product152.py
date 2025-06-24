# Leetcode 152
# Aufgabe ist, das Subarray mit dem größten Produkt zu finden.
class Solution:
    # Kadane's Algorithm

    # 2 Pointer laufen gegenläufig und berechnen jeweils die Produkte links oder rechts von einer potentiellen Null.
    # Es werden nur deswegen 2 Pointer genutzt weil es eine ungerade Anzahl an Minus-Vorzeichen geben kann.
    # Dies führt zu unterschiedlichen Ergebnissen.
    # Bspl.:
    # [2,-5,-2,-4,3]
    # von l nach r : 2*-5 =-10 *-2 = 20 * -4 = -80 * 3 = -240 , also max ist (20)
    # von r nach l : -4 *3 = -12 * -2 = 24 * -5 = -120 * 2 = -240 , also max ist (24)
    
    
    def max_product(self, nums):
        n =len(nums)
        left_product = 1
        right_product = 1
        ans = 0
        
        for i in range(n):
            # bei Ereichen einer Null wird das Produkt wieder neu gestartet mit einer 1 zum Multiplizieren.
            left_product = 1 if left_product == 0 else left_product
            right_product = 1 if right_product == 0 else right_product
            
            left_product *= nums[i]
            
            right_product *= nums[n -1 - i] # dies ist die Rückwärtsiteration in Python
            
            ans = max(ans, max(left_product, right_product))
            
        return ans
        
        
        
nums = [2, 3, -2, -5, 6, -1, 4]
nums2 = [2, 3, -2, 4, 0,-1, -3, 5]
nums3 = [2,-5,-2,-4,3]
sol = Solution()
print(sol.max_product(nums3))