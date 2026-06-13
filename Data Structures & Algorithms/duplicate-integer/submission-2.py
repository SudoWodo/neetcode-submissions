class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        D = set()
        for num in nums:
            if num in D:
                return True
            D.add(num)
        
        return False