# Leetcode 1   
# funktioniert mit dem hashset nur dann, wenn die Werte in nums einzigartig sind.
class Solution(object):
    def twoSum(self, nums, target):
        result = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] + nums[i] == target:
                    return [i,j]
                
                
# dies ist die Variante mit einem Hashset.         
    def two_Sum_Hash(self, nums, target):  
          num_map = {}
          for i, num in enumerate(nums):   # i ist der Index und num ist der Wert an der Index Stelle. Enumerate ist wie range(len(nums)), aber kürzer.
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i  # der Wert num ist der Key und der index i die Value



nums = [2,7,11,15]
target = 9
sol = Solution()
# print(sol.twoSum(nums,target))

print(sol.two_Sum_Hash(nums,target)) 