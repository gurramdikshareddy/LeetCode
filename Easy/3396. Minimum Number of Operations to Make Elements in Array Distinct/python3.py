class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        unique = set()
        operations = 0
        
        while len(nums) > len(set(nums)):
            nums = nums[3:]
            operations += 1
        
        return operations
