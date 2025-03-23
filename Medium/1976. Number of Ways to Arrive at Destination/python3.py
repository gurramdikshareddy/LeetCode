import heapq
from typing import List

MOD = 10**9 + 7

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        
        graph = [[] for _ in range(n)]
        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))
        
        dist = [float('inf')] * n
        ways = [0] * n
        dist[0] = 0
        ways[0] = 1  
        
        pq = [(0, 0)]  
        
        while pq:
            current_time, node = heapq.heappop(pq)
            
            if current_time > dist[node]:
                continue
            
            for neighbor, travel_time in graph[node]:
                new_time = current_time + travel_time
                
                
                if new_time < dist[neighbor]:
                    dist[neighbor] = new_time
                    ways[neighbor] = ways[node]
                    heapq.heappush(pq, (new_time, neighbor))
                
                elif new_time == dist[neighbor]:
                    ways[neighbor] = (ways[neighbor] + ways[node]) % MOD
        
        return ways[n-1]


solution = Solution()
n1 = 7
roads1 = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
print(solution.countPaths(n1, roads1))  
n2 = 2
roads2 = [[1,0,10]]
print(solution.countPaths(n2, roads2))  
