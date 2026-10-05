class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        ans = 0
        depth = 0
        
        for i in range(len(s)):
            if s[i] == '(':
                depth += 1
            else:
                depth -= 1
                # If we found a core "()", add 2^depth to the answer
                if s[i - 1] == '(':
                    ans += 1 << depth
                    
        return ans