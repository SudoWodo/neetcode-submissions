class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # bruteforce
        # for idx1 in range(len(nums)):
        #     for idx2 in range(len(nums)):
        #         if idx2 <= idx1 :
        #             continue
        #         if nums[idx1] + nums[idx2] == target:
        #             return [idx1, idx2]

        # return False


        # hash map method
        # why ? we are O(n^2)

        diff_dict = {}
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in diff_dict:
                return [diff_dict[diff], idx]
            else:
                diff_dict[num] = idx
