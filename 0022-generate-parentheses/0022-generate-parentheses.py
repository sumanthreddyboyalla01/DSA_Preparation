class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []

        def backtrack(current_str, open_count, close_count):
            # Base case: valid combination reached
            if len(current_str) == 2 * n:
                result.append(current_str)
                return

            # Add an opening parenthesis if we haven't reached n yet
            if open_count < n:
                backtrack(current_str + "(", open_count + 1, close_count)

            # Add a closing parenthesis if it wouldn't exceed open parentheses
            if close_count < open_count:
                backtrack(current_str + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return result