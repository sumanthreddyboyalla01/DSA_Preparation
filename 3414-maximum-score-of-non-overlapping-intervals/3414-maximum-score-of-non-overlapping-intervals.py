from bisect import bisect_left
from typing import List

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        # Store original index with interval data: (left, right, weight, original_index)
        sorted_intervals = sorted(
            [(intervals[i][0], intervals[i][1], intervals[i][2], i) for i in range(n)],
            key=lambda x: x[1]
        )
        
        # Extract right endpoints for binary search
        rights = [interval[1] for interval in sorted_intervals]
        
        # dp[k][i] = (max_score, sorted_list_of_indices) considering first i sorted intervals with at most k picks
        dp = [[(0, []) for _ in range(n + 1)] for _ in range(5)]
        
        for i in range(1, n + 1):
            l, r, w, orig_idx = sorted_intervals[i - 1]
            
            # Find the largest index j (1-based) where rights[j-1] < l
            # bisect_left finds first element >= l, so j is that index
            j = bisect_left(rights, l)
            
            for k in range(1, 5):
                # Option 1: Do not include the i-th sorted interval
                best_score, best_indices = dp[k][i - 1]
                
                # Option 2: Include the i-th sorted interval
                prev_score, prev_indices = dp[k - 1][j]
                cand_score = prev_score + w
                cand_indices = sorted(prev_indices + [orig_idx])
                
                # Compare Option 2 with Option 1
                if cand_score > best_score:
                    best_score = cand_score
                    best_indices = cand_indices
                elif cand_score == best_score and cand_score > 0:
                    if not best_indices or cand_indices < best_indices:
                        best_indices = cand_indices
                
                dp[k][i] = (best_score, best_indices)
        
        return dp[4][n][1]