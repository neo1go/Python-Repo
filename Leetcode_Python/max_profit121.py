# Leetcode 121
class Solution(object):
    # Brute Force Solution mit schlechter Laufzeit wegen zwei Schleifen
    """
    def best_time_to_sell_Stock(self, prices):
        n = len(prices)
        max_profit = 0
        
        for i in range(n-1):
            
            for j in range(i + 1, n):
                if prices[i]< prices[j]:
                    max_profit = max(max_profit,prices[j] - prices[i])
                    
        return max_profit
     """
# bessere Laufzeit durch eine einzelne Schleife 
    def best_time_to_sell_Stock(self, prices):
        buy_price = prices[0]
        profit = 0
        
        for i in range(len(prices)):
            if prices[i] < buy_price: # hier wird der neue niedrigste Kaufpreis gesetzt
                buy_price = prices[i]
            else: # tritt nur ein, wenn der Kaufpreis größer ist als der aktuelle Wert. Somit tritt ein Gewinn ein.
                current_profit = prices[i] - buy_price
                profit = max(current_profit, profit)
        
        return profit
        
        
nums1 = [7, 1, 5, 3, 6, 4]
nums2 = [7, 6, 4, 3, 1] # result = 0
nums3 = [7, 2, 4, 5, 1, 3, 6]

print(Solution().best_time_to_sell_Stock(nums1))