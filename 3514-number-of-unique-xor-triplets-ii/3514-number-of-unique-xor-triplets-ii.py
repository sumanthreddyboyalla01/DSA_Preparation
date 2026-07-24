class Solution:
    def uniqueXorTriplets(self, nums):
        MAX = 2048

        freq = [0] * MAX
        for x in nums:
            freq[x] = 1

        def fwht(a, inv=False):
            n = len(a)
            h = 1
            while h < n:
                for i in range(0, n, h * 2):
                    for j in range(i, i + h):
                        x = a[j]
                        y = a[j + h]
                        a[j] = x + y
                        a[j + h] = x - y
                h <<= 1
            if inv:
                for i in range(n):
                    a[i] //= n

        a = freq[:]
        fwht(a)

        
        for i in range(MAX):
            a[i] = a[i] * a[i] * a[i]

        fwht(a, True)

        ans = 0
        for v in a:
            if v != 0:
                ans += 1

        return ans