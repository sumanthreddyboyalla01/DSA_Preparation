class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        d = dict(knowledge)
        res = []
        key = []
        in_bracket = False
        
        for char in s:
            if char == '(':
                in_bracket = True
            elif char == ')':
                in_bracket = False
                key_str = "".join(key)
                res.append(d.get(key_str, "?"))
                key = []
            elif in_bracket:
                key.append(char)
            else:
                res.append(char)
                
        return "".join(res)