class Solution:
    def divideArray(self, nums):
        xor = 0
        for e in nums:
            xor ^= e

        if xor != 0:
            return False
        
        freq = [0] * 501
        for e in nums:
            freq[e] += 1

        for count in freq:
            if count % 2 != 0:
                return False

        return True
