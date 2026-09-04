class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        
        # Build suffix minimums array
        # min_suffix[i] stores min(nums[i..n-1])
        min_suffix = [0] * n
        min_suffix[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            min_suffix[i] = min(nums[i], min_suffix[i + 1])
            
        current_max = nums[0]
        
        # Iterate from left to right to find the first stable index
        for i in range(n):
            current_max = max(current_max, nums[i])
            instability_score = current_max - min_suffix[i]
            
            if instability_score <= k:
                return i
                
        return -1