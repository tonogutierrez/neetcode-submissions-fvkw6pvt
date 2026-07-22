class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxProfit = 0 
        for i in range(1, len(prices)):
            if prices[l] > prices[i]:
                l = i
            current = prices[i] - prices[l]
            maxProfit = max(maxProfit, current)
        return maxProfit 