class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def dfs(index, subset):
            # base condition
            if index == len(nums):
                result.append(subset.copy())
                return

            # choose
            subset.append(nums[index])
            dfs(index + 1, subset)

            # not choose
            subset.pop()
            dfs(index + 1, subset)
        
        dfs(0, [])

        return result