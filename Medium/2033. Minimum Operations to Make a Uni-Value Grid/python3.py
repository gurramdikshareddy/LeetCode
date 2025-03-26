from typing import List

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        
        flat = [num for row in grid for num in row]
        
        remainder = flat[0] % x
        for num in flat:
            if num % x != remainder:
                return -1
        
        flat.sort()
        median = flat[len(flat) // 2]
        
        operations = 0
        for num in flat:
            operations += abs(num - median) // x
        
        return operations
