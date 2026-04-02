class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        freq = [[] for i in range(len(nums)+1)]

        for n in nums:
            hashMap[n] = hashMap.get(n,0) + 1
        
        #number, repeated
        for x,i in hashMap.items():
            freq[i].append(x)
        
        ans = []

        for i in range(len(freq)-1,-1,-1):
            for n in freq[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans 
