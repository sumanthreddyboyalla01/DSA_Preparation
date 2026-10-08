class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        bal = 0
        
        for char in s:
            if char == '(':
                if bal > 0:
                    res.append(char)
                bal += 1
            else:
                bal -= 1
                if bal > 0:
                    res.append(char)
                    
        return "".join(res)