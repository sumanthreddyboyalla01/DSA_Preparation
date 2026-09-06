class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        
        # Base case: dp[0] = 1 (empty string t can be formed in 1 way)
        dp = [0] * (m + 1)
        dp[0] = 1
        
        for char_s in s:
            # Iterate backwards to avoid using updated values from the same iteration
            for j in range(m, 0, -1):
                if char_s == t[j - 1]:
                    dp[j] += dp[j - 1]
                    
        return dp[m]