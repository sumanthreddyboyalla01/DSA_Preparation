class Solution:
    def minOperations(self, s: str) -> int:
        if s == "".join(sorted(s)):
            return 0
        
        n = len(s)
        if n == 2:
            return -1
            
        mn = min(s)
        mx = max(s)
        
        # Check if min is at the start (excluding full string) or max is at the end
        if s[0] == mn or s[-1] == mx:
            return 1
            
        # Check if single max is at index 0 and single min is at index n-1
        if s.count(mx) == 1 and s[0] == mx and s.count(mn) == 1 and s[-1] == mn:
            return 3
            
        return 2