class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_needed = 0   # Unmatched closing brackets ')'
        close_needed = 0  # Unmatched opening brackets '('

        for char in s:
            if char == '(':
                close_needed += 1
            else:
                if close_needed > 0:
                    close_needed -= 1  # Match with an existing '('
                else:
                    open_needed += 1   # Unmatched ')', requires inserting a '('

        return open_needed + close_needed