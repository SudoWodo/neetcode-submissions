class Solution:
    def climbStairs(self, n: int) -> int:
        dp = dict()

        def compute(i):
            if i > n:
                return 0
            if i == n:
                return 1
            
            if i in dp:
                return dp[i]
            
            dp[i] = compute(i + 1) + compute(i + 2)

            return dp[i]
        
        return compute(0)
