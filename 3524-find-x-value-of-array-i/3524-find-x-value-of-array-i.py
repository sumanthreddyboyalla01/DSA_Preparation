class Solution:
    def resultArray(self, nums: list[int], k: int) -> list[int]:
        ans = [0] * k
        dp = [0] * k  # dp[r] stores count of contiguous subarrays ending at previous index with product % k == r
        
        for num in nums:
            val = num % k
            next_dp = [0] * k
            
            # Subarray consisting of only the current element
            next_dp[val] += 1
            
            # Extend existing subarrays
            for r in range(k):
                if dp[r] > 0:
                    next_dp[(r * val) % k] += dp[r]
            
            # Accumulate results and update DP state
            for r in range(k):
                ans[r] += next_dp[r]
            
            dp = next_dp
            
        return ans