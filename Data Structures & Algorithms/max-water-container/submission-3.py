class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L, R = 0, len(heights) - 1
        LeftMax, rightMax = 0 , 0
        maxWater = 0

        # to optimize
        # min(heights[L], heights[R]) * (R - L)

        while L < R:
            maxWater = max(min(heights[L], heights[R]) * (R - L), maxWater)

            if heights[L] < heights[R]:
                L +=  1

            else:
                R -= 1
            
        return maxWater

            

        