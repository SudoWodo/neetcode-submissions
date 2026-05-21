class Solution:
    def climbStairs(self, n: int) -> int:
        steps_count = {
            1 : 1,
            2 : 2
        }

        def count_steps(k):

            # base condtion
            if k <= 0:
                return 1
            if k in steps_count:
                return steps_count[k]
            
            s = count_steps(k-1) + count_steps(k-2)
            steps_count[k] = s
            return s

        return count_steps(n - 1) + count_steps(n-2) 