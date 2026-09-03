class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_val = min(nums1)
        
        # If the smallest element is odd, we can always make all elements odd (or all even)
        if min_val % 2 != 0:
            return True
        
        # If the smallest element is even, we can only succeed if there are NO odd numbers at all
        return all(x % 2 == 0 for x in nums1)