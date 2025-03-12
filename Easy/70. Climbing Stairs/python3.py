class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        return self._climbStairs(n, memo)
    
    def _climbStairs(self, n: int, memo: dict) -> int:
        if n == 0 or n == 1:
            return 1
        if n not in memo:
            memo[n] = self._climbStairs(n-1, memo) + self._climbStairs(n-2, memo)
        return memo[n]
