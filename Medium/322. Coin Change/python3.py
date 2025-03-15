class Solution:
    def coinChange(self, coins, amount):
        if amount == 0:
            return 0
        
        coins.sort()
        dp = [0] * (amount + 1)
        
        for i in range(1, amount + 1):
            j = 0
            while j < len(coins) and coins[j] <= i:
                if dp[i - coins[j]] == 0 and i - coins[j] != 0:
                    j += 1
                    continue
                
                temp = 1 + dp[i - coins[j]]
                if dp[i] != 0:
                    dp[i] = min(temp, dp[i])
                else:
                    dp[i] = temp
                j += 1
        
        if dp[amount] == 0:
            return -1
        
        return dp[amount]

