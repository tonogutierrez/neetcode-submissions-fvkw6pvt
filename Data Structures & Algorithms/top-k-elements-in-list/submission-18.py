class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = [[] for i in range(len(nums) + 1)]
        hashMap = {}

        for i in range(len(nums)):
            hashMap[nums[i]] = hashMap.get(nums[i],0) + 1
        
        for key, item in hashMap.items():
            arr[item].append(key)
        
        ans = []

        for i in range(len(arr)-1,0,-1):
            for n in arr[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans 