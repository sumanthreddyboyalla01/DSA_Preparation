class Solution:

    def checkValidString(self, s: str) -> bool:
        min_open = 0
        max_open = 0

        for char in s:
            if char == "(":
                min_open += 1
                max_open += 1
            elif char == ")":
                min_open -= 1
                max_open -= 1
            elif char == "*":
                min_open -= 1  # '*' treated as ')'
                max_open += 1  # '*' treated as '('

            # If max_open is negative, there are too many ')' to balance
            if max_open < 0:
                return False

            # min_open cannot drop below 0 (we can't have negative open brackets)
            if min_open < 0:
                min_open = 0

        # A valid string must be able to have 0 open brackets left over
        return min_open == 0