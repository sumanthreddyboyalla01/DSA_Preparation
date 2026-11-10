class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        # dp[j] stores the minimum cost to reach step j
        # We need steps from 0 to n, so size is n + 1
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        for j in range(1, n + 1):
            # We can jump to step j from i = j-1, j-2, j-3
            for i in range(max(0, j - 3), j):
                # costs[j-1] corresponds to costs[j] in 1-indexed notation
                cost_of_jump = costs[j - 1] + (j - i) ** 2
                dp[j] = min(dp[j], dp[i] + cost_of_jump)
                
        return dp[n]