class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        arraySet = set()

        for n in nums:
            if n in arraySet:
                return True

            arraySet.add(n)

        return False
