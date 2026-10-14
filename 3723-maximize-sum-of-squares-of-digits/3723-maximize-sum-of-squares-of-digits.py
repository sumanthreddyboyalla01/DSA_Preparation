class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum < 1 or sum > 9 * num:
            return ""
        
        res = [0] * num
        rem = sum
        
        # Greedily fill from left to right with 9s to maximize the leading digits
        for i in range(num):
            take = min(9, rem)
            res[i] = take
            rem -= take
            
        return "".join(map(str, res))