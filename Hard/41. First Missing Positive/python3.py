from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Remove all non-positive numbers
        nums = [n for n in nums if n > 0]

        # Sort the list
        nums.sort()

        target = 1
        for n in nums:
            if n == target:
                target += 1
            elif n > target:
                return target

        return target
