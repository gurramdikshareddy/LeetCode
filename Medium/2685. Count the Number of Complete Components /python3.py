from collections import defaultdict
from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        
        def dfs(node, visited, component):
            stack = [node]
            visited[node] = True
            while stack:
                u = stack.pop()
                component.append(u)
                for v in graph[u]:
                    if not visited[v]:
                        visited[v] = True
                        stack.append(v)
        
        visited = [False] * n
        complete_components = 0

        
        for i in range(n):
            if not visited[i]:
                component = []
                dfs(i, visited, component)

                
                k = len(component)
                edge_count = 0
                
                for u in component:
                    for v in graph[u]:
                        if u < v:  
                            edge_count += 1

                
                if edge_count == k * (k - 1) // 2:
                    complete_components += 1

        return complete_components
