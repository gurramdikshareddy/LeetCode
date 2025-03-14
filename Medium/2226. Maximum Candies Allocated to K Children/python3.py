class Solution:
    def maximumCandies(self, candies, k: int) -> int:
        left, right = 1, 10_000_000
        result = 0

        while left <= right:
            mid = left + (right - left) // 2
            childrenCount = 0

            for candy in candies:
                childrenCount += candy // mid

            if childrenCount >= k:
                result = mid
                left = mid + 1
            else:
                right = mid - 1

        return result
