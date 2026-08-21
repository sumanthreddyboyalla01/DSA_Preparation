from math import gcd

class Solution:
    def findKthSmallest(self, coins: list[int], k: int) -> int:

        def lcm(a, b):
            return a // gcd(a, b) * b

        def count(x):
            total = 0
            n = len(coins)

            for mask in range(1, 1 << n):
                cur_lcm = 1
                bits = 0
                valid = True

                for i in range(n):
                    if mask & (1 << i):
                        bits += 1
                        cur_lcm = lcm(cur_lcm, coins[i])

                        if cur_lcm > x:
                            valid = False
                            break

                if not valid:
                    continue

                value = x // cur_lcm

                if bits % 2:
                    total += value
                else:
                    total -= value

            return total

        lo = 1
        hi = min(coins) * k

        while lo < hi:
            mid = (lo + hi) // 2

            if count(mid) >= k:
                hi = mid
            else:
                lo = mid + 1

        return lo