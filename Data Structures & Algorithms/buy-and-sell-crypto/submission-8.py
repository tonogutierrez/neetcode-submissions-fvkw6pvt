class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        res = 0

        for i in range(1,len(prices)):
            if prices[l] > prices[i]:
                l = i
                continue 
            curr = prices[i] - prices[l]
            res = max(res, curr)
        return res 

        