class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        #7 - 3 = 4
        #7 - 4 = 3
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashMap:
                return [hashMap[diff],i]
            hashMap[nums[i]] = i
        
