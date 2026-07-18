class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = [[]for i in range(len(nums) + 1)]
        hashMap = {} # num - > cuanto se repite 

        for n in nums:
            hashMap[n] = hashMap.get(n,0) + 1

        for key, value in hashMap.items():
            arr[value].append(key)
        
        res = []

        for i in range(len(arr)-1,0,-1):
            for n in arr[i]:
                res.append(n)
                if len(res) == k:
                    return res 
        