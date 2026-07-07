class Solution(object):
    def sumAndMultiply(self, n):
        digits = [int(x) for x in str(n)]
        total = 0
        mult = []
        
        for digit in digits:
            total = total + digit
            if digit != 0:
                mult.append(digit)
        
        k = "".join(map(str, mult))
        s = int(k) if k else 0
        
        return s * total
