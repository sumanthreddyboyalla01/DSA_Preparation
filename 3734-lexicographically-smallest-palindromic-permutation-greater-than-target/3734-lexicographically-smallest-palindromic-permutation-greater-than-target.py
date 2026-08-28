class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        # Check palindrome feasibility
        odd = -1
        for i in range(26):
            if cnt[i] % 2:
                if odd != -1:
                    return ""
                odd = i

        half_len = n // 2
        half_cnt = [x // 2 for x in cnt]
        mid = chr(odd + 97) if n % 2 else ""

        def build(left_str):
            return left_str + mid + left_str[::-1]

        # 1. Try exact left-half match with target's left half
        left = []
        remaining = half_cnt[:]
        
        for i in range(half_len):
            t = ord(target[i]) - 97
            if remaining[t] > 0:
                remaining[t] -= 1
                left.append(target[i])
            else:
                break

        # If full left half matches target's left half
        if len(left) == half_len:
            candidate = build("".join(left))
            if candidate > target:
                return candidate

        # Helper to try replacing character at position idx with something > target_char
        def construct_greater(prefix_len, target_char):
            rem = half_cnt[:]
            # Consume prefix
            for k in range(prefix_len):
                rem[ord(left[k]) - 97] -= 1
            
            t = ord(target_char) - 97
            for c in range(t + 1, 26):
                if rem[c] > 0:
                    rem[c] -= 1
                    res = left[:prefix_len] + [chr(c + 97)]
                    for x in range(26):
                        res.extend([chr(x + 97)] * rem[x])
                    return build("".join(res))
            return None

        # 2. Try placing a larger character at the first mismatch index (if broke early)
        if len(left) < half_len:
            res = construct_greater(len(left), target[len(left)])
            if res:
                return res

        # 3. Backtrack from right to left along the matched prefix
        for i in range(len(left) - 1, -1, -1):
            res = construct_greater(i, left[i])
            if res:
                return res

        return ""