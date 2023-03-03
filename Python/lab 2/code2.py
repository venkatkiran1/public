class Solution:
    def maxProfit(prices):
        n = len(prices)
        dp = [0] * (n + 1)
        max_profit = 0
        for i in range(n):
            for j in range(i+1, n):
                profit = prices[j] - prices[i]
                dp[j] = max(dp[j], dp[i] + profit)
                max_profit = max(max_profit, dp[j])
        return max_profit


solution = Solution()
arr = [map(int, input().strip().split())]
print(solution.maxProfit(arr))
