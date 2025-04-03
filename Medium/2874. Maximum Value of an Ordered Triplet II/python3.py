class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        # Step-1: Find right_max for all indices
        right_max = [0] * n
        max_val = nums[-1]  # last element
        for i in range(n - 2, 0, -1):
            right_max[i] = max_val
            max_val = max(max_val, nums[i])
        
        # Step-2: Find max_triplet
        max_triplet = 0
        max_val = nums[0]
        for i in range(1, n - 1):
            max_triplet = max(max_triplet, (max_val - nums[i]) * right_max[i])
            max_val = max(max_val, nums[i])
        return max_triplet

# Alternative Python Solution (Optimized Space)
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_diff = 0
        max_left = 0
        max_val = 0
        for num in nums:
            max_val = max(max_val, max_diff * num)
            max_diff = max(max_diff, max_left - num)
            max_left = max(max_left, num)
        return max_val
