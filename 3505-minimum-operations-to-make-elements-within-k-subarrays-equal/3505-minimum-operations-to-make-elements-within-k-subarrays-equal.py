
class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        from bisect import bisect_left

        n = len(nums)

        # Coordinate compression
        vals = sorted(set(nums))
        m = len(vals)

        bit_count = [0] * (m + 1)
        bit_sum = [0] * (m + 1)

        def update(bit, i, delta):
            while i <= m:
                bit[i] += delta
                i += i & -i

        def query(bit, i):
            result = 0
            while i > 0:
                result += bit[i]
                i -= i & -i
            return result

        def kth(rank):
            idx = 0
            step = 1 << (m.bit_length() - 1)

            while step:
                nxt = idx + step
                if nxt <= m and bit_count[nxt] < rank:
                    idx = nxt
                    rank -= bit_count[nxt]
                step >>= 1

            return idx + 1

        # Calculate the cost of every window of size x
        costs = []

        for i, num in enumerate(nums):
            pos = bisect_left(vals, num) + 1

            update(bit_count, pos, 1)
            update(bit_sum, pos, num)

            if i >= x:
                old = nums[i - x]
                old_pos = bisect_left(vals, old) + 1

                update(bit_count, old_pos, -1)
                update(bit_sum, old_pos, -old)

            if i >= x - 1:
                mid_pos = kth((x + 1) // 2)
                median = vals[mid_pos - 1]

                left_count = query(bit_count, mid_pos)
                left_sum = query(bit_sum, mid_pos)

                total_sum = query(bit_sum, m)

                right_count = x - left_count
                right_sum = total_sum - left_sum

                cost = (
                    median * left_count - left_sum
                    + right_sum - median * right_count
                )

                costs.append(cost)

        # DP: minimum cost to select j windows
        INF = float('inf')

        dp_prev = [0] * (n + 1)

        for j in range(1, k + 1):
            dp_curr = [INF] * (n + 1)

            for i in range(1, n + 1):
                # Do not select a window ending at i
                dp_curr[i] = dp_curr[i - 1]

                # Select the window nums[i-x : i]
                if i >= x:
                    dp_curr[i] = min(
                        dp_curr[i],
                        dp_prev[i - x] + costs[i - x]
                    )

            dp_prev = dp_curr

        return dp_prev[n]
