class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        # Step 1: Find the first and last occurrence of each character
        first = {}
        last = {}
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i

        # Step 2: Find all valid valid substring ranges
        # A range [l, r] is valid if all occurrences of any character in s[l:r+1] are within [l, r]
        valid_intervals = []
        for ch in set(s):
            l, r = first[ch], last[ch]
            is_valid = True
            
            # Expand the range to cover all characters present within s[l:r+1]
            i = l
            while i <= r:
                if first[s[i]] < l:  # Character starts before current left boundary
                    is_valid = False
                    break
                r = max(r, last[s[i]])  # Extend right boundary if needed
                i += 1
            
            if is_valid:
                valid_intervals.append((l, r))

        # Step 3: Greedy Interval Scheduling
        # Sort intervals by end position to maximize count and minimize length
        valid_intervals.sort(key=lambda x: x[1])
        
        res = []
        prev_end = -1
        for l, r in valid_intervals:
            if l > prev_end:
                res.append(s[l:r + 1])
                prev_end = r

        return res