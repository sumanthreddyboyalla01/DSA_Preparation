from collections import defaultdict
from typing import List

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        
        # Get coordinates of all 1s in both images
        ones1 = [(r, c) for r in range(n) for c in range(n) if img1[r][c] == 1]
        ones2 = [(r, c) for r in range(n) for c in range(n) if img2[r][c] == 1]
        
        # Count frequency of translation vectors (dr, dc)
        vec_counts = defaultdict(int)
        max_overlap = 0
        
        for r1, c1 in ones1:
            for r2, c2 in ones2:
                # Vector required to shift (r1, c1) to (r2, c2)
                vec = (r2 - r1, c2 - c1)
                vec_counts[vec] += 1
                max_overlap = max(max_overlap, vec_counts[vec])
                
        return max_overlap