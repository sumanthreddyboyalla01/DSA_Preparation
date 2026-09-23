class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target = sum(nums) - x
        
        if target == 0:
            return len(nums)
        if target < 0:
            return -1
        
        prefix_map = {0: -1}  # prefix_sum -> index
        current_sum = 0
        max_len = -1
        
        for i, num in enumerate(nums):
            current_sum += num
            
            # Check if there is a prefix sum such that current_sum - prefix_sum = target
            if (current_sum - target) in prefix_map:
                max_len = max(max_len, i - prefix_map[current_sum - target])
                
            # Store first occurrence of current_sum to maximize distance
            if current_sum not in prefix_map:
                prefix_map[current_sum] = i
                
        return len(nums) - max_len if max_len != -1 else -1