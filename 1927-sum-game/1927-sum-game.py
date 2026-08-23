class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2

        left_sum = right_sum = 0
        left_q = right_q = 0

        for i in range(half):
            if num[i] == '?':
                left_q += 1
            else:
                left_sum += int(num[i])

        for i in range(half, n):
            if num[i] == '?':
                right_q += 1
            else:
                right_sum += int(num[i])

        # Odd number of '?' -> Alice can always force inequality
        if (left_q + right_q) % 2:
            return True

        diff = left_sum - right_sum
        qdiff = right_q - left_q

        # Bob can force equality
        if diff == 9 * qdiff // 2:
            return False

        return True