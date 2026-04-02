class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i,x in enumerate(nums):
            diff = target - nums[i] #7 - 3 = 4---- #7 - 4 = 3 
            if diff in hashMap:
                return [hashMap[diff],i]
            hashMap[x] = i