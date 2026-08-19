class Solution:
    def largestInteger(self, nums: list[int], k: int) -> int:
        freq = [0] * 51

        for i in range(len(nums) - k + 1):
            seen = set()

            for j in range(i, i + k):
                seen.add(nums[j])

            for x in seen:
                freq[x] += 1

        for x in range(50, -1, -1):
            if freq[x] == 1:
                return x

        return -1