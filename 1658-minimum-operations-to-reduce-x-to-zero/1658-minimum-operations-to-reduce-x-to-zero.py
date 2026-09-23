class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target = sum(nums) - x
        
        # If target is 0, we must pick all elements
        if target == 0:
            return len(nums)
        # If target < 0, it's impossible to sum to x
        if target < 0:
            return -1
        
        max_len = -1
        current_sum = 0
        left = 0
        
        for right in range(len(nums)):
            current_sum += nums[right]
            
            # Shrink window if the sum exceeds target
            while current_sum > target and left <= right:
                current_sum -= nums[left]
                left += 1
                
            if current_sum == target:
                max_len = max(max_len, right - left + 1)
                
        return len(nums) - max_len if max_len != -1 else -1