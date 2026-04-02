class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashTable = set()
        for x in nums:
            if x in hashTable:
                return True
            hashTable.add(x)
        return False
         