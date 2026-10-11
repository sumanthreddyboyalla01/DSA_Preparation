class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = 0
        
        for i in range(1, n + 1):
            if n % i == 0:
                # Since Python is 0-indexed, the element at 1-indexed position i is at nums[i - 1]
                total_sum += nums[i - 1] ** 2
                
        return total_sum