class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(i, subset):

            # Base case
            if i == len(nums):
                result.append(subset.copy())
                return
            
            # include case
            subset.append(nums[i])
            dfs(i+1, subset)

            subset.pop()
            dfs(i + 1, subset)
        
        dfs(0, [])

        return result