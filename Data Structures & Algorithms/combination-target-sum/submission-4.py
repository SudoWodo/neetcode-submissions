class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        subset = []
        result = []
        
        def dfs(idx, curSum):

            if curSum == target:
                result.append(subset.copy())
                return 

            if idx >= len(nums):
                return

            # choose
            subset.append(nums[idx])
            if curSum + nums[idx] <= target:
                dfs(idx , curSum + nums[idx])
            
            # choose next
            subset.pop()
            dfs(idx + 1, curSum)

        dfs(0,0)
        return result
        