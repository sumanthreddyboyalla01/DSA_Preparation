class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        bit_counts = [0] * 31
        
        # Count the frequency of each set bit across all numbers
        for x in nums:
            for b in range(31):
                if (x >> b) & 1:
                    bit_counts[b] += 1
                    
        # Construct the k largest possible numbers
        max_nums = [0] * k
        for i in range(k):
            current_val = 0
            for b in range(31):
                if bit_counts[b] > 0:
                    current_val |= (1 << b)
                    bit_counts[b] -= 1
            max_nums[i] = current_val
            
        # Calculate the sum of squares modulo 10^9 + 7
        total_sum = 0
        for x in max_nums:
            total_sum = (total_sum + x * x) % MOD
            
        return total_sum