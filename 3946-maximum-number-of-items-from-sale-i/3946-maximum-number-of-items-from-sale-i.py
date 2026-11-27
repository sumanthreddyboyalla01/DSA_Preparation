class Solution:
    def maximumSaleItems(self, items: list[list[int]], budget: int) -> int:
        n = len(items)
        free_bonus = [0] * n

        for i in range(n):
            fi, _ = items[i]
            cnt = 0
            for j in range(n):
                if i != j and items[j][0] % fi == 0:
                    cnt += 1
            free_bonus[i] = cnt

        dp = [0] * (budget + 1)

        for i in range(n):
            _, price = items[i]
            if price > budget:
                continue

            bonus = 1 + free_bonus[i]
            for b in range(budget, price - 1, -1):
                if dp[b - price] + bonus > dp[b]:
                    dp[b] = dp[b - price] + bonus

            for b in range(price, budget + 1):
                if dp[b - price] + 1 > dp[b]:
                    dp[b] = dp[b - price] + 1

        return dp[budget]