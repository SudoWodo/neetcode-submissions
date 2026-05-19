class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ## brute force approch

        area = 0
        for left, height in enumerate(heights):
            for right in range(left + 1, len(heights)):
                area = max(
                    (right - left) * min(height, heights[right]), 
                    area
                    )
        
        return area