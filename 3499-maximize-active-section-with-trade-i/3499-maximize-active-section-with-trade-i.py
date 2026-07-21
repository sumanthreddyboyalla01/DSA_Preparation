from itertools import groupby

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        ones = s.count('1')
        t = "1" + s + "1"

        runs = [(ch, len(list(g))) for ch, g in groupby(t)]

        best = 0
        for i in range(1, len(runs) - 1):
            if (
                runs[i][0] == '1'
                and runs[i - 1][0] == '0'
                and runs[i + 1][0] == '0'
            ):
                best = max(best, runs[i - 1][1] + runs[i + 1][1])

        return ones + best