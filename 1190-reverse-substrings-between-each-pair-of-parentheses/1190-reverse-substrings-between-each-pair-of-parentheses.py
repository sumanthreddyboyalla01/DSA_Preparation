class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        pair = {}
        stack = []
        
        # Precompute matching parenthesis indices
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                j = stack.pop()
                pair[i] = j
                pair[j] = i
                
        result = []
        curr = 0
        direction = 1  # 1 for forward, -1 for backward
        
        # Traverse string and teleport across matching parentheses
        while curr < n:
            if s[curr] in '()':
                curr = pair[curr]
                direction = -direction
            else:
                result.append(s[curr])
            curr += direction
            
        return "".join(result)