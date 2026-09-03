import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        bestk = 1

        while left <= right:
            mid = (left + right) // 2
            # print(f"left: {left} , right {right}, mid : {mid}")
            hours = 0
            for bananas in piles:
                hours += math.ceil(bananas / mid)
            # print(f"hours: {hours} at rate : {mid}")

            if hours <= h:
                right = mid - 1
                bestk = mid
            else:
                left = mid + 1
                    
        return bestk
            