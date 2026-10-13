class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # Square all elements and sort them
        squares = sorted(x * x for x in nums)
        n = len(squares)
        
        # The first half (smaller values) are subtracted, the second half (larger values) are added
        mid = n // 2
        return sum(squares[mid:]) - sum(squares[:mid])