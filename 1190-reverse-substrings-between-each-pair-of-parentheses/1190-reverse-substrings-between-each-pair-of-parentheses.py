class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        
        for char in s:
            if char == ')':
                # Pop characters until matching '(' is found
                rev = []
                while stack and stack[-1] != '(':
                    rev.append(stack.pop())
                stack.pop()  # Remove '('
                
                # Push reversed characters back onto the stack
                stack.extend(rev)
            else:
                stack.append(char)
                
        return "".join(stack)