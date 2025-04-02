from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        max_k = [0] * n  # To store the maximum nums[k] for k >= current index

        # Precompute the maximum value from the end
        max_k[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            max_k[i] = max(max_k[i + 1], nums[i])

        max_value = 0

        # Iterate through the array to find the maximum triplet value
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] > nums[j] and j + 1 < n:  # Ensure we don't go out of bounds
                    # Find the maximum nums[k] for k > j
                    max_value = max(max_value, (nums[i] - nums[j]) * max_k[j + 1])

        return max_value
