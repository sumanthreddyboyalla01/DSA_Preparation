import math

class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7

        def helper(arr):
            if len(arr) <= 2:
                return 1
            
            root = arr[0]
            left = [x for x in arr if x < root]
            right = [x for x in arr if x > root]
            
            # Ways to interleave left and right subtrees while preserving relative order
            ways_comb = math.comb(len(left) + len(right), len(left)) % MOD
            
            ways_left = helper(left)
            ways_right = helper(right)
            
            return (ways_comb * ways_left * ways_right) % MOD

        # Subtract 1 because the original array arrangement is not a "reordering"
        return (helper(nums) - 1) % MOD