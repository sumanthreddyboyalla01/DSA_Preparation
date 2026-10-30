import heapq
from collections import defaultdict
from typing import List

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            
        # Min-heap stores: (cost, node, consecutive_count)
        pq = [(0, 0, 1)]
        
        # Best cost to reach (node, count)
        # Using a dict or 2D array: dist[node][count]
        dist = {}
        
        while pq:
            cost, u, count = heapq.heappop(pq)
            
            if u == n - 1:
                return cost
                
            if (u, count) in dist and dist[(u, count)] < cost:
                continue
                
            for v, w in graph[u]:
                # Determine new consecutive count
                if labels[u] == labels[v]:
                    new_count = count + 1
                else:
                    new_count = 1
                    
                if new_count > k:
                    continue
                    
                next_cost = cost + w
                
                if (v, new_count) not in dist or next_cost < dist[(v, new_count)]:
                    dist[(v, new_count)] = next_cost
                    heapq.heappush(pq, (next_cost, v, new_count))
                    
        return -1