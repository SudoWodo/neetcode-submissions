class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result = []
        prefix = 1
        # prefix products
        for idx in range(len(nums)):
            result.append(prefix)
            prefix *= nums[idx]
        
        suffix = 1
        for idx in range(len(nums) - 1, -1, -1):
            result[idx] *= suffix
            suffix *= nums[idx]
        return result