import re

class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        d = dict(knowledge)
        return re.sub(r'\((.*?)\)', lambda m: d.get(m.group(1), '?'), s)