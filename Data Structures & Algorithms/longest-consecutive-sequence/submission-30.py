class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0 
        arr = set(nums)

        for n in arr:
            if n-1 not in arr:
                length = 1
                while n + length in arr:
                    length += 1
                longest = max(longest, length)
        return longest 