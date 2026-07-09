class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        res = 0 
        currentProfit = 0 

        for r in range(l+1,len(prices)):
            if prices[l] > prices[r]:
                l = r
                continue
            currentProfit = prices[r] - prices[l]
            res = max(res, currentProfit)
        return res 
            
