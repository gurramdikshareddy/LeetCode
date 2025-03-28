import heapq

class Solution:
    def maxPoints(self, grid, queries):
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        n = len(queries)
        result = [0] * n
        visited = [[0] * cols for _ in range(rows)]

        min_heap = []
        sorted_queries = [(queries[i], i) for i in range(n)]
        sorted_queries.sort(key=lambda x: x[0])

        heapq.heappush(min_heap, (grid[0][0], 0, 0))
        visited[0][0] = 1
        points = 0

        for query_val, query_idx in sorted_queries:
            while min_heap and min_heap[0][0] < query_val:
                top = heapq.heappop(min_heap)
                row, col = top[1], top[2]
                points += 1

                for dir in directions:
                    nr, nc = row + dir[0], col + dir[1]
                    if 0 <= nr < rows and 0 <= nc < cols and visited[nr][nc] == 0:
                        heapq.heappush(min_heap, (grid[nr][nc], nr, nc))
                        visited[nr][nc] = 1
            
            result[query_idx] = points
        
        return result
