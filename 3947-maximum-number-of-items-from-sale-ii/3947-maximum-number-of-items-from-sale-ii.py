class Solution:
    def maximumSaleItems(self, items: list[list[int]], budget: int) -> int:
        max_f = max(f for f, _ in items)
        min_price = min(p for _, p in items)

        freq = [0] * (max_f + 1)
        for f, _ in items:
            freq[f] += 1

        # mult_count[d] = number of items whose factor is a multiple of d
        mult_count = [0] * (max_f + 1)
        for d in range(1, max_f + 1):
            total = 0
            for m in range(d, max_f + 1, d):
                total += freq[m]
            mult_count[d] = total

        # Only consider boosted copies when their cost per pair doesn't lose
        # to buying cheap items at min_price (at most 2 items per boosted copy)
        boosted = []
        for f, p in items:
            gain = mult_count[f] - 1
            if gain > 0 and p <= 2 * min_price:
                boosted.append((p, gain))

        boosted.sort(key=lambda x: x[0])

        ans = 0
        rem = budget
        for p, gain in boosted:
            if rem < p:
                break
            take = min(gain, rem // p)
            ans += take * 2
            rem -= take * p

        ans += rem // min_price
        return ans