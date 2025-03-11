class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        low, high = -1, sum(nums)
        ans = -1

        if len(nums) < k:
            return -1
        
        for num in nums:
            low = max(low, num)
        
        while low <= high:
            mid = low + (high - low) // 2
            partition = self.findDistribution(nums, mid)
            if partition <= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans
    
    def findDistribution(self, arr: list[int], max_sum: int) -> int:
        partition = 1
        total = 0
        
        for num in arr:
            if total + num <= max_sum:
                total += num
            else:
                partition += 1
                total = num
        
        return partition
