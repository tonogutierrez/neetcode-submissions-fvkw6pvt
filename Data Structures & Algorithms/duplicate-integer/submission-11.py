class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hasDuplicate = set()

        for x in nums:
            if x in hasDuplicate:
                return True
            hasDuplicate.add(x)
        return False 
            