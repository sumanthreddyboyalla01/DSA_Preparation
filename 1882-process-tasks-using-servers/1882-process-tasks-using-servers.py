import heapq

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        n = len(servers)
        m = len(tasks)
        
        # Min-heap of available servers: stores tuples of (weight, index)
        free_servers = [(servers[i], i) for i in range(n)]
        heapq.heapify(free_servers)
        
        # Min-heap of busy servers: stores tuples of (free_time, weight, index)
        busy_servers = []
        
        ans = []
        current_time = 0
        
        for j in range(m):
            # Advance current time to at least j if all servers are busy and no tasks are waiting
            current_time = max(current_time, j)
            
            # If no servers are available, fast-forward time to when the earliest server becomes free
            if not free_servers:
                current_time = busy_servers[0][0]
            
            # Release all servers that have finished their tasks by current_time
            while busy_servers and busy_servers[0][0] <= current_time:
                free_time, weight, index = heapq.heappop(busy_servers)
                heapq.heappush(free_servers, (weight, index))
            
            # Assign the current task (j) to the best available server
            weight, index = heapq.heappop(free_servers)
            ans.append(index)
            
            # Push the server into the busy heap with its new free time
            heapq.heappush(busy_servers, (current_time + tasks[j], weight, index))
            
        return ans