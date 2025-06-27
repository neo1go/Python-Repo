# Leetcode 53
# Es wird das größte zusammenhängende Subarray gesucht.
# Dazu kann man Memoization nutzen.
# Ist die Addition an Stelle in der Iteration kleiner als der aktuelle Wert an der Indexstelle, so wird der Wert neu gesetzt.
# Bspl.:
# [-2, 2, 2, -3, 7]
# -2 u 2 = 0  2+2 = 4    4 -3 =1  (bis jetzt ist 4 der Max Wert) -> 4 -3  = 1  Max ist im Moment 4   -> 7    7 ist endgültige Max Wert
# wenn also eine Addition ein größerer Wert ist, so wird er beibehalten, andernfalls wird der aktuelle Wert genommen.
class Solution(object):
    def maxSubArray(self, nums):
        max_so_far = nums[0]
        current_max = nums[0]

        for num in nums[1:]:
            
            current_max = max(num, current_max + num)# entweder der aktuelle Wert oder die voherige Addition. Die wichtigste Stelle hier.
                                                     # so wird ein schlechterer niedriger Wert automatisch überschrieben bzw. ignoriert.
            max_so_far = max(max_so_far, current_max) 
        return max_so_far


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
nums1 = [-2, 2, 2, -4, 7]
print(Solution().maxSubArray(nums1))
