class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low1 = 0
        profit = 0
        for i in range(len(prices)):
            if prices[i] < prices[low1]:
                low1 = i
            if (prices[i] - prices[low1] > profit):
                profit = prices[i] - prices[low1]
        return profit