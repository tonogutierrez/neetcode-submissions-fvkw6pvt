class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = [[] for i in range(len(nums) + 1)]
        hashMap = {} #num - repeated

        for n in nums:
            hashMap[n] = hashMap.get(n,0) + 1
        
        for index, num in hashMap.items():
            arr[num].append(index)
        
        res = []

        for i in range(len(arr)-1,0,-1):
            for n in arr[i]:
                res.append(n)
                if len(res) == k:
                    return res
