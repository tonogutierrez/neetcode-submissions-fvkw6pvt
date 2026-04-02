class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        arr = []

        for n in nums:
            hashMap[n] = 1 + hashMap.get(n,0)
        
        for n,c in hashMap.items():
            arr.append([c,n])
        
        arr.sort()
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        
        return res
        
