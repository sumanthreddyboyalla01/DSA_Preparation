from collections import deque
from typing import List

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        
        start_x = start_y = -1
        litter_coords = []
        
        # Parse grid to find 'S' and all 'L' positions
        for r in range(m):
            for c in range(n):
                cell = classroom[r][c]
                if cell == 'S':
                    start_x, start_y = r, c
                elif cell == 'L':
                    litter_coords.append((r, c))
        
        litter_map = {pos: i for i, pos in enumerate(litter_coords)}
        num_litter = len(litter_coords)
        full_mask = (1 << num_litter) - 1
        
        # Check if start position is already on a litter (if any)
        start_mask = 0
        if (start_x, start_y) in litter_map:
            start_mask |= (1 << litter_map[(start_x, start_y)])
            
        if start_mask == full_mask:
            return 0
        
        # best_energy[x][y][mask] stores max remaining energy for (x, y, mask)
        best_energy = [[[-1] * (1 << num_litter) for _ in range(n)] for _ in range(m)]
        best_energy[start_x][start_y][start_mask] = energy
        
        # Queue format: (x, y, mask, current_energy, steps)
        queue = deque([(start_x, start_y, start_mask, energy, 0)])
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        while queue:
            x, y, mask, e, steps = queue.popleft()
            
            if mask == full_mask:
                return steps
            
            if e == 0:
                continue
                
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                # Check grid boundaries and obstacles
                if 0 <= nx < m and 0 <= ny < n and classroom[nx][ny] != 'X':
                    next_e = e - 1
                    next_mask = mask
                    cell = classroom[nx][ny]
                    
                    # Pick up litter
                    if cell == 'L':
                        next_mask |= (1 << litter_map[(nx, ny)])
                    # Energy reset
                    elif cell == 'R':
                        next_e = energy
                    
                    # Only proceed if we found a strictly greater energy state
                    if next_e > best_energy[nx][ny][next_mask]:
                        best_energy[nx][ny][next_mask] = next_e
                        queue.append((nx, ny, next_mask, next_e, steps + 1))
                        
        return -1