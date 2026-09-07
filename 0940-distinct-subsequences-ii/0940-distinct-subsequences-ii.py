class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        # Stores the number of distinct subsequences ending with each letter
        last_added = [0] * 26
        
        for char in s:
            idx = ord(char) - ord('a')
            # New subsequences formed by appending 'char' to all existing subsequences + 1 (for 'char' itself)
            last_added[idx] = (sum(last_added) + 1) % MOD
            
        return sum(last_added) % MOD