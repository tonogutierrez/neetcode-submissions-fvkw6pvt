class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        arr = []
        for i in range(len(nums)):
            hashMap[nums[i]] = 1 + hashMap.get(nums[i],0)
        
        for n,c in hashMap.items():
            arr.append([c,n])
        
        arr.sort()
        res = []

        while k > len(res):
            res.append(arr.pop()[1])
        return res 