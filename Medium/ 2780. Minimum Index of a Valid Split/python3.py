from collections import Counter

class Solution:
    def minimumIndex(self, nums: list[int]) -> int:
        n = len(nums)
        
        counter = Counter(nums)
        dominant_element = max(counter, key=lambda x: counter[x])
        
        prefix_count = [0] * n
        suffix_count = [0] * n
        
        count = 0
        for i in range(n):
            if nums[i] == dominant_element:
                count += 1
            prefix_count[i] = count
        
        count = 0
        for i in range(n-1, -1, -1):
            if nums[i] == dominant_element:
                count += 1
            suffix_count[i] = count
        
        # Now, check for valid splits
        for i in range(n - 1):  # Split can only happen from 0 to n-2
            left_count = prefix_count[i]
            right_count = suffix_count[i + 1]
            if left_count > (i + 1) // 2 and right_count > (n - i - 1) // 2:
                return i
        
        return -1
