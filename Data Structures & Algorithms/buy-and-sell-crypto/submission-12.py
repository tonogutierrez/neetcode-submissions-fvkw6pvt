class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0 
        l = 0 

        for r in range(1,len(prices)):
            if prices[r] > prices[l]:
                currentProfit = prices[r] - prices[l]
                maxProfit = max(maxProfit,currentProfit)
            else:
                l = r
        return maxProfit 