class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in nums:

            if num - 1 not in num_set:
                length = 1
                start = num

                while start + 1 in num_set:
                    length += 1
                    start = start + 1

                longest = max(longest, length)
        
        return longest