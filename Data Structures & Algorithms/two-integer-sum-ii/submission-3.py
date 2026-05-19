class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        diff_hash = dict()
        for idx, num in enumerate(numbers):
            diff = target - num
            if diff in diff_hash:
                return [diff_hash[diff] + 1, idx + 1]
            else:
                diff_hash[num] = idx