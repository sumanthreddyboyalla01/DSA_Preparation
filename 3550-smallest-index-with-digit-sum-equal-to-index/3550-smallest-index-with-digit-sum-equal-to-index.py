class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        # Maximum digit sum for nums[i] <= 1000 is 1 + 0 + 0 + 0 = 1, or 9+9+9 = 27
        limit = min(len(nums), 28)
        
        for i in range(limit):
            val = nums[i]
            digit_sum = sum(map(int, str(val)))
            if digit_sum == i:
                return i
                
        return -1