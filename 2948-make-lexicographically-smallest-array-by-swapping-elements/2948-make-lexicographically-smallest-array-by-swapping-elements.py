class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        # Pair elements with their original indices and sort by value
        sorted_pairs = sorted([(val, i) for i, val in enumerate(nums)])
        
        result = [0] * n
        group_vals = []
        group_indices = []
        
        for i in range(n):
            # If starting a new group or difference exceeds limit
            if i > 0 and sorted_pairs[i][0] - sorted_pairs[i - 1][0] > limit:
                # Place sorted values into original indices for the current group
                group_indices.sort()
                for idx, val in zip(group_indices, group_vals):
                    result[idx] = val
                
                # Reset group lists
                group_vals = []
                group_indices = []
            
            group_vals.append(sorted_pairs[i][0])
            group_indices.append(sorted_pairs[i][1])
        
        # Process the final group
        group_indices.sort()
        for idx, val in zip(group_indices, group_vals):
            result[idx] = val
            
        return result