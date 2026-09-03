class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        for idx in range(len(height)):
            leftMax = 0
            rightMax = 0

            for leftIdx in range(idx):
                leftMax = max(height[leftIdx], leftMax)
            
            for rightIdx in range(idx, len(height)):
                rightMax = max(height[rightIdx], rightMax)
            
            water += max((min(leftMax, rightMax) - height[idx]), 0)
        return water