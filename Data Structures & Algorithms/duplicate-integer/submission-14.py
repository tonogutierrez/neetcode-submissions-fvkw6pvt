class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        rnums = set()

        for n in nums:
            if n in rnums:
                return True 
            rnums.add(n)
        return False 