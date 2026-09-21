from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        
        # Use left < right so that the loop terminates when left == right
        while left < right:
            mid = (left + right) // 2
            
            # If the middle element is greater than the rightmost element,
            # the minimum element must be in the right un-sorted portion.
            if nums[mid] > nums[right]:
                left = mid + 1
            # Otherwise, the minimum element is at mid or to its left side.
            else:
                right = mid
                
        # When left == right, they both point to the minimum element.
        return nums[left]
