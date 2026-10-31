class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        
        # Memoization for jump targets: memo[(r, c, direction)] -> (target_r, target_c) or None
        memo = {}

        def get_jump(r, c, d):
            # d: 0 for Right (dx=0, dy=1), 1 for Down (dx=1, dy=0)
            state = (r, c, d)
            if state in memo:
                return memo[state]
            
            # Initial step
            if d == 0:
                nr, nc, dx, dy = r, c + 1, 0, 1
            else:
                nr, nc, dx, dy = r + 1, c, 1, 0
            
            # Path tracking for memoization compression
            path = []
            while 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                path.append((nr, nc, dx, dy))
                if dy == 1:
                    dx, dy = 1, 0
                else:
                    dx, dy = 0, 1
                nr, nc = nr + dx, nc + dy
            
            if 0 <= nr < m and 0 <= nc < n:
                res = (nr, nc)
            else:
                res = None
            
            memo[state] = res
            return res

        # DP table
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        for r in range(m):
            for c in range(n):
                if dp[r][c] == 0:
                    continue
                
                current_ways = dp[r][c]
                
                # Try moving Right (d=0) and Down (d=1)
                for d in range(2):
                    nxt = get_jump(r, c, d)
                    if nxt is not None:
                        nr, nc = nxt
                        dp[nr][nc] = (dp[nr][nc] + current_ways) % MOD

        return dp[m - 1][n - 1]