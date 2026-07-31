from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = sorted(Counter(word).values(), reverse=True)

        ans = 0
        for i in range(len(freq)):
            ans += freq[i] * (i // 8 + 1)

        return ans