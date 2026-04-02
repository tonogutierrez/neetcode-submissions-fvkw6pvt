class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {} #number, repeated 
        freq= [[]for i in range(len(nums)+1)]

        for x in nums:
            counter[x] = 1 + counter.get(x,0)
        for i,n in counter.items():
            freq[n].append(i)
        ans = []
        for i in range(len(freq)-1,-1,-1):
            for n in freq[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans