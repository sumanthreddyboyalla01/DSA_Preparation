class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = float("inf")

        # cost[i][j] = min changes to make s[i..j] a semi-palindrome
        cost = [[INF] * n for _ in range(n)]

        for i in range(n):
            for j in range(i + 1, n):  # semi-palindrome requires length >= 2
                length = j - i + 1
                best = INF

                # d is a proper divisor of length (1 <= d < length)
                for d in range(1, length):
                    if length % d != 0:
                        continue

                    changes = 0
                    for start in range(d):
                        # Group indices: i + start, i + start + d, ... <= j
                        left = i + start
                        # Last index in this group <= j
                        steps = (j - left) // d
                        right = left + steps * d

                        while left < right:
                            if s[left] != s[right]:
                                changes += 1
                            left += d
                            right -= d

                    if changes < best:
                        best = changes

                cost[i][j] = best

        # dp[i][p] = min changes to split s[0..i] into p semi-palindromes
        dp = [[INF] * (k + 1) for _ in range(n)]

        for i in range(1, n):
            dp[i][1] = cost[0][i]

        for p in range(2, k + 1):
            # Need at least 2 chars per segment -> end index needs at least 2*p - 1
            for end in range(2 * p - 1, n):
                # Previous partition must end at `cut` with at least 2*(p-1)-1 index,
                # and current segment [cut + 1 .. end] must have length >= 2
                for cut in range(2 * (p - 1) - 1, end - 1):
                    if dp[cut][p - 1] != INF and cost[cut + 1][end] != INF:
                        candidate = dp[cut][p - 1] + cost[cut + 1][end]
                        if candidate < dp[end][p]:
                            dp[end][p] = candidate

        return int(dp[n - 1][k])