class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        min_len = [float('inf')] * n
        
        ans = float('inf')
        curr_sum = 0
        left = 0
        min_so_far = float('inf')
        
        for right in range(n):
            curr_sum += arr[right]
            
            # Shrink window if sum exceeds target
            while curr_sum > target and left <= right:
                curr_sum -= arr[left]
                left += 1
            
            # Found a valid sub-array
            if curr_sum == target:
                curr_len = right - left + 1
                
                # Check if a non-overlapping subarray exists before 'left'
                if left > 0 and min_len[left - 1] != float('inf'):
                    ans = min(ans, curr_len + min_len[left - 1])
                
                min_so_far = min(min_so_far, curr_len)
            
            min_len[right] = min_so_far
            
        return ans if ans != float('inf') else -1