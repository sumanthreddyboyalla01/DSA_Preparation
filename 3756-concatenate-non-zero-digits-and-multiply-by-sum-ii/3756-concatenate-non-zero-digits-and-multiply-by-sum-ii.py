class Solution:
    def sumAndMultiply(self, s, queries):

        MOD = 1000000007
        n = len(s)

        cnt = [0] * (n + 1)
        sm = [0] * (n + 1)
        val = [0] * (n + 1)
        pow10 = [1] * (n + 1)

        for i in range(1, n + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD


        for i in range(n):

            d = ord(s[i]) - 48

            cnt[i + 1] = cnt[i]
            sm[i + 1] = sm[i]
            val[i + 1] = val[i]

            if d != 0:
                cnt[i + 1] += 1
                sm[i + 1] += d
                val[i + 1] = (val[i] * 10 + d) % MOD


        ans = []

        for q in queries:

            l = q[0]
            r = q[1]

            length = cnt[r + 1] - cnt[l]

            x = (
                val[r + 1]
                - val[l] * pow10[length]
            ) % MOD

            total = sm[r + 1] - sm[l]

            ans.append((x * total) % MOD)


        return ans