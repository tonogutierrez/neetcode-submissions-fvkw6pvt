class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        arr = []
        for n in nums:
            hashMap[n] = 1 + hashMap.get(n,0)
        
        for n, c in hashMap.items():
            arr.append([c,n])
        arr.sort() #Lo ordena por el valor de n que se repite

        ans = []

        while len(ans) < k:
            ans.append(arr.pop()[1])
        return ans 