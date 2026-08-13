class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: list[int]) -> list[int]:
        n = len(s)
        size = 1

        while size < n:
            size <<= 1

        # left_char, right_char, prefix, suffix, best, length
        tree = [None] * (2 * size)

        for i, ch in enumerate(s):
            tree[size + i] = (ch, ch, 1, 1, 1, 1)

        for i in range(size - 1, 0, -1):
            tree[i] = self.merge(tree[2 * i], tree[2 * i + 1])

        ans = []

        for ch, idx in zip(queryCharacters, queryIndices):
            pos = size + idx
            tree[pos] = (ch, ch, 1, 1, 1, 1)

            pos //= 2
            while pos:
                tree[pos] = self.merge(tree[2 * pos], tree[2 * pos + 1])
                pos //= 2

            ans.append(tree[1][4])

        return ans

    def merge(self, a, b):
        if a is None:
            return b
        if b is None:
            return a

        lc, rc, lp, ls, lb, llen = a
        lc2, rc2, rp, rs, rb, rlen = b

        prefix = lp
        suffix = rs
        best = max(lb, rb)

        if rc == lc2:
            best = max(best, ls + rp)

            # Entire left segment has one character
            if lp == llen:
                prefix = llen + rp

            # Entire right segment has one character
            if rs == rlen:
                suffix = rlen + ls

        return (
            lc,
            rc2,
            prefix,
            suffix,
            best,
            llen + rlen
        )