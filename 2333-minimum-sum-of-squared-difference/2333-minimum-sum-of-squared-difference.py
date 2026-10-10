class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        n = len(nums1)
        total_k = k1 + k2
        
        # Calculate initial absolute differences and their frequencies
        diff_count = {}
        max_diff = 0
        for a, b in zip(nums1, nums2):
            d = abs(a - b)
            if d > 0:
                diff_count[d] = diff_count.get(d, 0) + 1
                if d > max_diff:
                    max_diff = d
                    
        # If total difference sum is already reducible to 0 or no operations needed
        if max_diff == 0 or total_k == 0:
            return sum(d * d for d in diff_count.keys() for _ in range(diff_count[d]))
            
        # Greedily reduce from max_diff down to 1
        curr = max_diff
        while curr > 0 and total_k > 0:
            if curr not in diff_count:
                curr -= 1
                continue
                
            count = diff_count[curr]
            # Operations needed to bring all elements of 'curr' down to 'curr - 1'
            take = min(total_k, count)
            
            total_k -= take
            diff_count[curr] -= take
            diff_count[curr - 1] = diff_count.get(curr - 1, 0) + take
            
            if take < count:
                # We ran out of operations (total_k == 0)
                break
            curr -= 1
            
        # Calculate the final minimum sum of squared differences
        ans = 0
        for d, count in diff_count.items():
            ans += (d * d) * count
            
        return ans