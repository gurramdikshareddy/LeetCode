class Solution:
    def canStealKHouses(self, nums, k, capability):
        count = 0
        i = 0
        while i < len(nums):
            if nums[i] <= capability:
                count += 1
                i += 2
            else:
                i += 1
        return count >= k
    
    def minCapability(self, nums, k):
        left = min(nums)
        right = max(nums)
        
        while left < right:
            mid = left + (right - left) // 2
            if self.canStealKHouses(nums, k, mid):
                right = mid
            else:
                left = mid + 1
        
        return left
