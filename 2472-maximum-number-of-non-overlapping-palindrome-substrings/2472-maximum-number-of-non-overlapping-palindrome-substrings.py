class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0
        last_end = -1  # Tracks the end index of the last chosen palindrome

        # Expand around centers
        for i in range(2 * n - 1):
            l = i // 2
            r = l + (i % 2)

            while l >= 0 and r < n and s[l] == s[r]:
                length = r - l + 1

                # Check if palindrome meets length requirement and doesn't overlap
                if length >= k:
                    if l > last_end:
                        ans += 1
                        last_end = r
                    break  # Greedily stop expanding once we find the shortest valid palindrome for this center

                l -= 1
                r += 1

        return ans