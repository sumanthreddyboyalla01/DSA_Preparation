import bisect
import heapq

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        # Min-heap to store (end_time, server_id) of busy servers
        busy = []
        
        # List of available servers, initially all 0 to k-1
        available = list(range(k))
        
        # Track the request count for each server
        counts = [0] * k
        
        for i, start_time in enumerate(arrival):
            # 1. Free up servers that have finished their tasks by the current arrival time
            while busy and busy[0][0] <= start_time:
                _, server_id = heapq.heappop(busy)
                # Insert back into available servers while maintaining sorted order
                bisect.insort(available, server_id)
            
            # If no servers are available, the request is dropped
            if not available:
                continue
            
            # 2. Find the first available server >= (i % k)
            target = i % k
            idx = bisect.bisect_left(available, target)
            
            # If no server >= target is found, wrap around and pick the first available server
            if idx == len(available):
                idx = 0
            
            server_id = available.pop(idx)
            
            # 3. Assign the task to this server
            counts[server_id] += 1
            heapq.heappush(busy, (start_time + load[i], server_id))
            
        # 4. Find the maximum requests handled by any server
        max_handled = max(counts)
        
        # Return all servers that handled the maximum number of requests
        return [i for i, c in enumerate(counts) if c == max_handled]