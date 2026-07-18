class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0 
        numSet = set(nums)
        #[2,20,4,10,3,4,5]
        for n in numSet:
            if n - 1 not in numSet:
                long = 1
                while n + long in numSet:
                    long += 1
                longest = max(long, longest)
        return longest 