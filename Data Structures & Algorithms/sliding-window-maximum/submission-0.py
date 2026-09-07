class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        _max = float('-inf')
        result = []
        left = 0

        for right in range(len(nums)):

            _max = max(_max, nums[right])

            if right - left + 1 >= k:
                result.append(_max)
                left += 1
            
            # print(_max, result)
        return result

            


