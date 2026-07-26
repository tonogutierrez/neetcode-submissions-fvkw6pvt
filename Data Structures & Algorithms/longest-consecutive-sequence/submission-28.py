class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0 
        numList = set(nums)

        for n in numList:
            counter = 0
            if n-1 in numList:
                counter = 1
            while n + counter in numList:
                counter += 1
            res = max(res, counter)
        return res 