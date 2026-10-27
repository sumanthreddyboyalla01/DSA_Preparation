class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = []
        
        # Row 0: All free cells '.' except maybe the last one
        # Actually, the path goes right along row 0, then down the last column.
        # So row 0 should be all '.' if n=1 or if it's part of the route.
        for i in range(m):
            if i == 0:
                # First row: all free '.'
                grid.append("." * n)
            else:
                # For all other rows, block everything except the last column
                grid.append("#" * (n - 1) + ".")
                
        return grid