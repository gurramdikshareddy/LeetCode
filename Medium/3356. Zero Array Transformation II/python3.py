class Solution:
    def minZeroArray(self, nums, queries):
        n = len(nums)

        # Check if all elements are already zero
        if all(x == 0 for x in nums):
            return 0

        left, right = 1, len(queries)
        
        # Check if it's possible to make the array zero with all queries
        if not self.canMakeZeroArray(right, nums, queries):
            return -1
        
        # Binary search to find the minimum k
        while left < right:
            mid = left + (right - left) // 2
            if self.canMakeZeroArray(mid, nums, queries):
                right = mid
            else:
                left = mid + 1
        
        return left

    def canMakeZeroArray(self, k, nums, queries):
        n = len(nums)
        diff = [0] * (n + 1)
        
        # Apply the first k queries
        for i in range(k):
            left, right, val = queries[i]
            diff[left] += val
            if right + 1 < n:
                diff[right + 1] -= val
        
        curr_val = 0
        for i in range(n):
            curr_val += diff[i]
            if curr_val < nums[i]:
                return False
        
        return True
