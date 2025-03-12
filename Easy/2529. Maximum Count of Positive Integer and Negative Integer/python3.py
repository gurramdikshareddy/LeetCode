class Solution:
    def maximumCount(self, nums):
        negCount = self.binarySearch(nums, 0)
        posCount = len(nums) - self.binarySearch(nums, 1)
        return max(negCount, posCount)

    def binarySearch(self, nums, target):
        left, right = 0, len(nums) - 1
        result = len(nums)

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                result = mid
                right = mid - 1
        
        return result
