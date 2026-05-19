class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # bruteforce
        result = []
        for idx1 in range(len(nums)):
            prod = 1
            for idx2 in range(len(nums)):
                if idx1 == idx2:
                    continue
                prod *= nums[idx2]
            
            result.append(prod)
        
        return result