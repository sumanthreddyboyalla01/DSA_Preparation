class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        # Total steps from (0,0) to (m-1, n-1) is m + n - 1
        # A valid parentheses string must have an even length
        if (m + n - 1) % 2 != 0:
            return False
        
        # Path must start with '(' and end with ')'
        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False
        
        # Maximum possible balance at any point is (m + n - 1) // 2
        max_bal = (m + n - 1) // 2
        
        # dp[r][c] stores a set of possible net open-bracket balances at grid[r][c]
        dp = [[set() for _ in range(n)] for _ in range(m)]
        
        # Starting point
        dp[0][0].add(1)
        
        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0:
                    continue
                
                delta = 1 if grid[r][c] == '(' else -1
                
                # Gather incoming balances from top and left neighbors
                prev_balances = set()
                if r > 0:
                    prev_balances.update(dp[r - 1][c])
                if c > 0:
                    prev_balances.update(dp[r][c - 1])
                
                # Update current cell's possible balances
                for bal in prev_balances:
                    new_bal = bal + delta
                    if 0 <= new_bal <= max_bal:
                        dp[r][c].add(new_bal)
        
        # Check if balance 0 is reachable at the bottom-right cell
        return 0 in dp[m - 1][n - 1]