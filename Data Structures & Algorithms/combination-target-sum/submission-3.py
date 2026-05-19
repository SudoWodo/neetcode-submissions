class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []

        def dfs(index ,total, subset):

            if total == target:
                results.append(subset.copy())
                return
            
            elif (total > target):
                return
            elif index >= len(nums):
                return
            else:
                
                # retry the index
                subset.append(nums[index])
                dfs(index, total + nums[index], subset)

                # Try new index
                subset.pop()
                dfs(index + 1, total, subset)

        dfs(0, 0, [])
        return results
