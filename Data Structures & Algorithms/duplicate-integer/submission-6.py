class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashMap = {}


        for x in nums:
            if x in hashMap:
                return True
            hashMap[x] = 1 + hashMap.get(x,0)
        return False