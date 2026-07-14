from typing import List
from math import gcd

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        MAXV = 200
        g = [[0] * (MAXV + 1) for _ in range(MAXV + 1)]
        for a in range(MAXV + 1):
            for b in range(1, MAXV + 1):
                g[a][b] = b if a == 0 else gcd(a, b)

        dp = [[0] * (MAXV + 1) for _ in range(MAXV + 1)]
        dp[0][0] = 1

        for x in nums:
            ndp = [[0] * (MAXV + 1) for _ in range(MAXV + 1)]
            for g1 in range(MAXV + 1):
                row = dp[g1]
                for g2 in range(MAXV + 1):
                    cur = row[g2]
                    if cur == 0:
                        continue

                    ndp[g1][g2] = (ndp[g1][g2] + cur) % MOD

                    
                    ng1 = g[g1][x]
                    ndp[ng1][g2] = (ndp[ng1][g2] + cur) % MOD

                    
                    ng2 = g[g2][x]
                    ndp[g1][ng2] = (ndp[g1][ng2] + cur) % MOD

            dp = ndp

        ans = 0
        for d in range(1, MAXV + 1):
            ans = (ans + dp[d][d]) % MOD

        return ans