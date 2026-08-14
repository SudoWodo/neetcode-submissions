class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # num -> index
        memory = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in memory:
                    return [memory[diff], i]
            memory[num] = i