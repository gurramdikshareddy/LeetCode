from typing import List

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        # Helper function to check if it's possible to repair all cars within a given time
        def canRepairAllCars(time):
            total_cars_repaired = 0
            for rank in ranks:
                # Max cars a mechanic can repair in given 'time'
                max_cars = int((time / rank) ** 0.5)
                total_cars_repaired += max_cars
                if total_cars_repaired >= cars:
                    return True
            return total_cars_repaired >= cars

        # Binary search for the minimum time
        low, high = 0, min(ranks) * cars * cars
        while low < high:
            mid = (low + high) // 2
            if canRepairAllCars(mid):
                high = mid  # Try smaller time
            else:
                low = mid + 1  # Increase time
        
        return low
