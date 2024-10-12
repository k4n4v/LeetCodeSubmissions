class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy, sell = 0, 1
        max_profit = 0
        
        while sell < len(prices):
            if prices[sell] > prices[buy]: # if selling price is greater than buying
                profit =  prices[sell] - prices[buy] # profit margin
                max_profit = max(max_profit, profit) 
            else:
                buy = sell 
            sell += 1
        
        return max_profit
    
    # Time: O(n)
    # Space: O(1)