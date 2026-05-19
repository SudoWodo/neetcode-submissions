class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(idx, subset):
            
            # base condition
            if idx == len(nums):
                result.append(subset.copy())
                return 


            subset.append(nums[idx])
            dfs(idx + 1, subset)

            subset.pop()
            dfs(idx + 1, subset)
            
        dfs(0, [])

        return result
