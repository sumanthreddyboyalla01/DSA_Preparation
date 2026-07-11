from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        ans = 0

        for i in range(n):
            if visited[i]:
                continue

            stack = [i]
            visited[i] = True
            component = []

            while stack:
                node = stack.pop()
                component.append(node)
                for nei in graph[node]:
                    if not visited[nei]:
                        visited[nei] = True
                        stack.append(nei)

            k = len(component)
            complete = True
            for node in component:
                if len(graph[node]) != k - 1:
                    complete = False
                    break

            if complete:
                ans += 1

        return ans