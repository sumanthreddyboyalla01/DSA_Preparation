class Solution:
    def pathExistenceQueries(self, n, nums, maxDiff, queries):

        arr = sorted((nums[i], i) for i in range(n))

        pos = [0] * n
        values = [0] * n

        for i, pair in enumerate(arr):
            val, idx = pair
            pos[idx] = i
            values[i] = val


        nxt = [0] * n
        r = 0

        for l in range(n):
            while r + 1 < n and values[r + 1] - values[l] <= maxDiff:
                r += 1

            nxt[l] = r


        LOG = 18

        jump = [[0] * n for _ in range(LOG)]

        for i in range(n):
            jump[0][i] = nxt[i]


        for k in range(1, LOG):
            for i in range(n):
                jump[k][i] = jump[k-1][jump[k-1][i]]


        ans = []

        for query in queries:

            u = query[0]
            v = query[1]

            a = pos[u]
            b = pos[v]

            if a > b:
                a, b = b, a


            if a == b:
                ans.append(0)
                continue


            if jump[LOG-1][a] < b:
                ans.append(-1)
                continue


            cur = a
            steps = 0

            for k in range(LOG-1, -1, -1):
                if jump[k][cur] < b:
                    cur = jump[k][cur]
                    steps += (1 << k)

            ans.append(steps + 1)


        return ans