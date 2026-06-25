class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles) #1.....9
        res = r

        while l <= r:
            k = (l + r) // 2
            acc = 0 
            for p in piles:
                acc += math.ceil(p/k)
            
            if acc <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res 

