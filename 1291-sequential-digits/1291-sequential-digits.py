class Solution:
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        result = []
        digits = "123456789"
        
        # Determine the length boundaries based on low and high
        min_len = len(str(low))
        max_len = len(str(high))
        
        # Sliding window over the digits string
        for length in range(min_len, max_len + 1):
            for start in range(10 - length):
                num = int(digits[start:start + length])
                if low <= num <= high:
                    result.append(num)
                    
        return result