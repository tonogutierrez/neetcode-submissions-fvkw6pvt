class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles) #1............4

        res = r

        while l <= r:
            k = (l + r) // 2 #cuanto va a comer
            hours = 0 

            for p in piles:
                hours += math.ceil(p/k)
            
            if hours <= h:
                res = k 
                r = k - 1

            else:
                l = k + 1
        return res 