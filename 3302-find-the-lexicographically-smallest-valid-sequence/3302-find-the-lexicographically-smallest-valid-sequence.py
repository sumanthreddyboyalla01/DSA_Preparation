class Solution:
    def validSequence(self, word1: str, word2: str):
        n = len(word1)
        m = len(word2)

        # dp[i] = maximum number of characters of word2
        # that can be matched from word1[i:] using exact matches.
        dp = [0] * (n + 1)

        j = m - 1
        for i in range(n - 1, -1, -1):
            dp[i] = dp[i + 1]

            if j >= 0 and word1[i] == word2[j]:
                dp[i] += 1
                j -= 1

        ans = [0] * m
        i = j = 0

        # Greedily construct lexicographically smallest indices.
        while i < n and j < m:
            if word1[i] == word2[j]:
                ans[j] = i
                j += 1
            else:
                # Use the one allowed mismatch if the remaining
                # characters can still be matched exactly.
                if dp[i + 1] >= m - j - 1:
                    ans[j] = i
                    j += 1
                    i += 1
                    break

            i += 1

        # Match the remaining suffix exactly.
        while i < n and j < m:
            if word1[i] == word2[j]:
                ans[j] = i
                j += 1
            i += 1

        return ans if j == m else []