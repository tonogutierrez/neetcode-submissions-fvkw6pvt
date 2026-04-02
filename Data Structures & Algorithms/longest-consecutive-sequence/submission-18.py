class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0 
        
        nums.sort()
        current = nums[0]
        streak = 0
        res = 0 

        i = 0 

        while i < len(nums):
            if current != nums[i]:
                current = nums[i]
                streak = 0
            while i < len(nums) and current == nums[i]:
                i += 1
            streak += 1
            current += 1
            res = max(res,streak)
        return res 