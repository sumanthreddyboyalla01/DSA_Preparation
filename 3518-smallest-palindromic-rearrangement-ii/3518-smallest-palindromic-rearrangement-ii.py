from collections import Counter
from math import comb

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        cnt = Counter(s)

        half = [0] * 26
        mid = ""

        for c, v in cnt.items():
            idx = ord(c) - 97
            half[idx] = v // 2
            if v & 1:
                mid = c

        LIMIT = k

        def ways(freq):
            total = sum(freq)
            res = 1
            rem = total
            for x in freq:
                if x:
                    res *= comb(rem, x)
                    if res > LIMIT:
                        return LIMIT + 1
                    rem -= x
            return res

        if ways(half) < k:
            return ""

        left = []
        rem = sum(half)

        for _ in range(rem):
            for i in range(26):
                if half[i] == 0:
                    continue

                half[i] -= 1
                cnt_perm = ways(half)

                if cnt_perm >= k:
                    left.append(chr(i + 97))
                    break

                k -= cnt_perm
                half[i] += 1

        left = "".join(left)
        return left + mid + left[::-1]