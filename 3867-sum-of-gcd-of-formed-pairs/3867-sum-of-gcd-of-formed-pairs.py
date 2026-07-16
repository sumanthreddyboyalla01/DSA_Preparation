from typing import List
from math import gcd

class Solution:
    def gcdSum(self, nums: List[int]) -> int:
        prefix_gcd = []
        mx = 0

        for x in nums:
            mx = max(mx, x)
            prefix_gcd.append(gcd(x, mx))

        prefix_gcd.sort()

        ans = 0
        i, j = 0, len(prefix_gcd) - 1

        while i < j:
            ans += gcd(prefix_gcd[i], prefix_gcd[j])
            i += 1
            j -= 1

        return ans