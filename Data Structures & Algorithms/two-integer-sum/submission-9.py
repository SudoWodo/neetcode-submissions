class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_look_up = {}
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in sum_look_up:
                return [sum_look_up[diff], idx]
            else:
                sum_look_up[num] = idx
