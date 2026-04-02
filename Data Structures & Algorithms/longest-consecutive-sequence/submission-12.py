class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0 
        
        nums.sort()
        res = 0 
        streak = 0
        current = nums[0]

        i = 0
        while i < len(nums):
            if current != nums[i]:
                current = nums[i]
                streak = 0
            while i<len(nums) and nums[i] == current :
                i += 1
            streak += 1
            current += 1
            res = max(streak,res)
        return res