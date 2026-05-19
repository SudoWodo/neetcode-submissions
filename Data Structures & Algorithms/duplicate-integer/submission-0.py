class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup_dict = {}
        for num in nums:
            if num in dup_dict:
                return True
            else:
                dup_dict[num] = 1
        
        return False
