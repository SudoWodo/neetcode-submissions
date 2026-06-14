class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        subset = []

        def dfs(idx, curSum):
            ## base condition
            if curSum == target:
                result.append(subset.copy())
                return 

            ## for loop
            for i in range(idx, len(nums)):

                if curSum + nums[i] <= target:
                    subset.append(nums[i])
                    dfs(i , curSum + nums[i])
                    subset.pop()
         
        dfs(0,0)
        return result