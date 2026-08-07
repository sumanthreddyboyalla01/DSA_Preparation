class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        # Step 1: Prime factorize t into powers of 2, 3, 5, 7
        temp_t = t
        cnt = {2: 0, 3: 0, 5: 0, 7: 0}
        for p in [2, 3, 5, 7]:
            while temp_t % p == 0:
                cnt[p] += 1
                temp_t //= p
        
        # If t has prime factors > 7, no digit product can ever be divisible by t
        if temp_t > 1:
            return "-1"

        # Helper to find minimum digit representation for required prime powers
        def get_needed_digits(c2, c3, c5, c7):
            best_digits = None
            # c2 <= 50, c3 <= 30 for t <= 10^14
            for c8 in range(c2 // 3 + 2):
                for c9 in range(c3 // 2 + 2):
                    for c6 in range(min(c2, c3) + 2):
                        rem_2 = max(0, c2 - 3 * c8 - c6)
                        rem_3 = max(0, c3 - 2 * c9 - c6)
                        
                        c4 = rem_2 // 2
                        r2 = rem_2 % 2
                        r3 = rem_3
                        
                        digits = (
                            [8] * c8 + [9] * c9 + [6] * c6 +
                            [4] * c4 + [2] * r2 + [3] * r3 +
                            [5] * c5 + [7] * c7
                        )
                        
                        digits.sort()
                        if best_digits is None or len(digits) < len(best_digits) or (
                            len(digits) == len(best_digits) and digits < best_digits
                        ):
                            best_digits = digits
            return best_digits

        def consume(c2, c3, c5, c7, d):
            if d == 2: c2 = max(0, c2 - 1)
            elif d == 3: c3 = max(0, c3 - 1)
            elif d == 4: c2 = max(0, c2 - 2)
            elif d == 5: c5 = max(0, c5 - 1)
            elif d == 6:
                c2 = max(0, c2 - 1)
                c3 = max(0, c3 - 1)
            elif d == 7: c7 = max(0, c7 - 1)
            elif d == 8: c2 = max(0, c2 - 3)
            elif d == 9: c3 = max(0, c3 - 2)
            return c2, c3, c5, c7

        n = len(num)
        
        # Compute prefix requirement states up to the first '0'
        pref_req = [(cnt[2], cnt[3], cnt[5], cnt[7])]
        first_zero = n
        
        for idx, ch in enumerate(num):
            if ch == '0':
                first_zero = idx
                break
            d = int(ch)
            r2, r3, r5, r7 = pref_req[-1]
            pref_req.append(consume(r2, r3, r5, r7, d))

        # Check if num itself is valid (only possible if no zeros in num)
        if first_zero == n and pref_req[n] == (0, 0, 0, 0):
            return num

        # Try to find a matching prefix of length n
        # We can only branch off at index i <= first_zero
        for i in range(min(n - 1, first_zero), -1, -1):
            req2, req3, req5, req7 = pref_req[i]
            
            # Start digit must be strictly greater than num[i]
            # If num[i] was '0', we can try digits starting from '1'
            start_digit = int(num[i]) + 1 if num[i] != '0' else 1
            rem_len = n - 1 - i
            
            for d in range(start_digit, 10):
                nr2, nr3, nr5, nr7 = consume(req2, req3, req5, req7, d)
                needed = get_needed_digits(nr2, nr3, nr5, nr7)
                
                if len(needed) <= rem_len:
                    prefix = num[:i] + str(d)
                    suffix_digits = [1] * (rem_len - len(needed)) + needed
                    suffix_digits.sort()
                    return prefix + "".join(map(str, suffix_digits))

        # If no valid number of length n exists, construct the smallest valid number of length n + 1 (or min length needed for factors)
        needed = get_needed_digits(cnt[2], cnt[3], cnt[5], cnt[7])
        target_len = max(n + 1, len(needed))
        
        result_digits = [1] * (target_len - len(needed)) + needed
        result_digits.sort()
        return "".join(map(str, result_digits))