class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        arr = [[] for i in range(len(nums) + 1)]

        for n in nums:
            hashMap[n] = 1 + hashMap.get(n,0)

        for n , i in hashMap.items():
            arr[i].append(n)
        
        res = []

        for i in range(len(arr)-1,0,-1):
            for n in arr[i]:
                res.append(n)
                if len(res) == k:
                    return res