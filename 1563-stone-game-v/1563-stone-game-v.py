class Solution:
    def stoneGameV(self, stoneValue: list[int]) -> int:
        n = len(stoneValue)

        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        dp = [[0] * n for _ in range(n)]

        # left_best[l][r]:
        # max(dp[l][m] + sum(l..m)) for m <= r
        left_best = [[0] * n for _ in range(n)]

        # right_best[l][r]:
        # max(dp[m][r] + sum(m..r)) for m >= l
        right_best = [[0] * n for _ in range(n)]

        for i in range(n):
            left_best[i][i] = stoneValue[i]
            right_best[i][i] = stoneValue[i]

        for length in range(2, n + 1):
            for l in range(n - length + 1):
                r = l + length - 1

                total = prefix[r + 1] - prefix[l]

                # Find largest m such that
                # sum(l..m) <= sum(m+1..r)
                lo = l
                hi = r - 1

                while lo <= hi:
                    m = (lo + hi) // 2
                    left_sum = prefix[m + 1] - prefix[l]

                    if left_sum * 2 <= total:
                        lo = m + 1
                    else:
                        hi = m - 1

                boundary = hi

                best = 0

                # left_sum <= right_sum
                if boundary >= l:
                    best = left_best[l][boundary]

                # Exact equality:
                if boundary >= l:
                    left_sum = prefix[boundary + 1] - prefix[l]

                    if left_sum * 2 == total:
                        best = max(
                            best,
                            right_best[boundary + 1][r]
                        )

                # left_sum > right_sum
                if boundary + 1 <= r - 1:
                    best = max(
                        best,
                        right_best[boundary + 2][r]
                    )

                dp[l][r] = best

                # Update left-side maximum
                current = dp[l][r] + total

                left_best[l][r] = max(
                    left_best[l][r - 1],
                    current
                )

                # Update right-side maximum
                right_best[l][r] = max(
                    right_best[l + 1][r],
                    current
                )

        return dp[0][n - 1]