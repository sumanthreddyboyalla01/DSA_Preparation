class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, val in enumerate(nums):
            if sum(int(digit) for digit in str(val)) == i:
                return i
        return -1