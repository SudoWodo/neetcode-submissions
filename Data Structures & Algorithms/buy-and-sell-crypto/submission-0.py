class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ## brute force
        current_max = 0
        for idx1, first in enumerate(prices):
            for second in prices[idx1: ]:
                if second - first > current_max:
                    current_max = second - first

        return current_max
                

