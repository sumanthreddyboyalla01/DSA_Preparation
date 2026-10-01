class Solution:
    def isValid(self, s: str) -> bool:
        # Dictionary to map closing brackets to their corresponding opening brackets
        matching_bracket = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            if char in matching_bracket:
                # Pop the top element if stack is non-empty, else assign dummy value '#'
                top_element = stack.pop() if stack else '#'
                
                # Check if the popped element matches the expected opening bracket
                if matching_bracket[char] != top_element:
                    return False
            else:
                # Push opening brackets onto the stack
                stack.append(char)

        # If stack is empty, all brackets were valid and properly matched
        return not stack