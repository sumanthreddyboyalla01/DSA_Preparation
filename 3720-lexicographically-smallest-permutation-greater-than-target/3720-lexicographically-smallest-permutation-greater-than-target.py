class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)

        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        # used = characters consumed by matching target prefix
        used = [0] * 26

        best = ""

        for i in range(n):
            cur = ord(target[i]) - ord('a')

            
            for c in range(cur + 1, 26):
                if cnt[c] - used[c] > 0:

                    remaining = cnt[:]

                    
                    for j in range(i):
                        remaining[ord(target[j]) - ord('a')] -= 1

                    
                    remaining[c] -= 1

                    candidate = target[:i] + chr(c + ord('a'))

                    for x in range(26):
                        candidate += chr(x + ord('a')) * remaining[x]

                    
                    if best == "" or candidate < best:
                        best = candidate

            
            if cnt[cur] - used[cur] == 0:
                break

            used[cur] += 1

        return best