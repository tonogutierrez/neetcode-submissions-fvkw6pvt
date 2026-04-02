class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashMap = {}

        for n in nums:
            if n in hashMap:
                return True
            hashMap[n] = hashMap.get(n,0) + 1
        return False
        