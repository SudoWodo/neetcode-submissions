class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lookup = dict()
        for idx, num in enumerate(numbers, 1):
            diff = target - num
            if diff in lookup:
                return [lookup[diff], idx]
            else:
                lookup[num] = idx
