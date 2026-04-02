class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        arr = []

        for n in nums:
            hashMap[n] = 1 + hashMap.get(n,0)

        #number, repeated
        for x,i in hashMap.items():
            arr.append([i,x])
        
        arr.sort()
        res = []

        while k > len(res):
            res.append(arr.pop()[1])
        return res 