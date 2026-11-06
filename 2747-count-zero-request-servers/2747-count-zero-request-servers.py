from typing import List

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        # Sort logs by timestamp
        logs.sort(key=lambda l: l[1])
        
        # Pair queries with their original indices and sort by query time
        m = len(queries)
        indexed_queries = sorted(enumerate(queries), key=lambda q: q[1])
        
        ans = [0] * m
        active_servers = {} # server_id -> frequency in current window
        
        left = 0
        right = 0
        num_logs = len(logs)
        
        for orig_idx, q in indexed_queries:
            window_start = q - x
            window_end = q
            
            # Expand right pointer to include logs up to window_end
            while right < num_logs and logs[right][1] <= window_end:
                s_id = logs[right][0]
                active_servers[s_id] = active_servers.get(s_id, 0) + 1
                right += 1
                
            # Move left pointer to exclude logs older than window_start
            while left < num_logs and logs[left][1] < window_start:
                s_id = logs[left][0]
                active_servers[s_id] -= 1
                if active_servers[s_id] == 0:
                    del active_servers[s_id]
                left += 1
                
            # Total servers - servers that received at least one request = servers with zero requests
            ans[orig_idx] = n - len(active_servers)
            
        return ans