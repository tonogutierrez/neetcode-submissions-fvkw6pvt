class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = [[] for i in range(len(nums) + 1)]
        hashMap = {}

        for n in nums:
            hashMap[n] = 1 + hashMap.get(n,0)
        
        for num, index in hashMap.items():
            arr[index].append(num)
        
        res = []
        for i in range(len(arr)-1,0,-1):
            for n in arr[i]:
                res.append(n)
                if len(res) == k:
                    return res