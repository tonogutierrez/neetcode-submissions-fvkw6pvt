class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = [0] * len(nums)
        prefix = 1 

        for i in range(len(nums)):
            arr[i] = prefix
            prefix *= nums[i]

        prof = 1
        for i in range(len(nums)-1,-1,-1):
            arr[i] *= prof
            prof *= nums[i]
        return arr 