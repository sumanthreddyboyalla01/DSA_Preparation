from collections import Counter
from typing import List

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        digit_counts = Counter(digits)
        valid_count = 0
        
        # Iterate over all possible 3-digit even numbers
        for num in range(100, 1000, 2):
            d1, d2, d3 = num // 100, (num // 10) % 10, num % 10
            num_counts = Counter([d1, d2, d3])
            
            # Check if digit requirements can be satisfied by `digits`
            if all(digit_counts[d] >= count for d, count in num_counts.items()):
                valid_count += 1
                
        return valid_count