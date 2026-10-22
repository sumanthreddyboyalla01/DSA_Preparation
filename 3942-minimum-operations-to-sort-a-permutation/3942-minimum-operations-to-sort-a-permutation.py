from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)

        if nums == list(range(n)):
            return 0

        k = nums[0]

        # Check cyclic rotations of the sorted array.
        rotation = all(
            nums[i] == (k + i) % n
            for i in range(n)
        )

        # Check cyclic rotations of the reversed sorted array.
        reflection = all(
            nums[i] == (k - i) % n
            for i in range(n)
        )

        if rotation or reflection:
            return min(n - k, k + 2)

        return -1