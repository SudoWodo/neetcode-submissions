class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # create left max array
        leftMin = float('inf')
        maxP = 0
        for p in prices:
            leftMin = min(leftMin, p)
            maxP = max(maxP, p - leftMin)
        
        return maxP