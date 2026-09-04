class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        smallest = float('inf')
        for price in prices:
            smallest = min(price, smallest)
            max_profit = max(max_profit, price - smallest)
        
        return max_profit
                