class Solution:
    def missingMultiple(self, nums, k):
        nums_set = set(nums)

        x = k
        while x in nums_set:
            x += k

        return x