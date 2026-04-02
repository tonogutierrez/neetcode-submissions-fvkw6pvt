class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}

        for n in nums:
            hashMap[n]  = 1 + hashMap.get(n,0)

        arr = []
        for number, index in hashMap.items():
            arr.append([index,number])
        arr.sort()

        res = []
        while len(res) < k :
            res.append(arr.pop()[1])

        return res 
