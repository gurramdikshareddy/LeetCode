from typing import List

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1 or k == len(weights):
            return 0
        
        # Create two lists to store the sums of adjacent weights
        sum1 = [weights[i] + weights[i+1] for i in range(len(weights) - 1)]
        sum2 = sum1.copy()

        # Sort sum1 in ascending order and sum2 in descending order
        sum1.sort()
        sum2.sort(reverse=True)

        # Calculate the sums of the first (k-1) elements
        ans1 = sum(sum1[:k-1])
        ans2 = sum(sum2[:k-1])

        # Return the difference
        return ans2 - ans1
