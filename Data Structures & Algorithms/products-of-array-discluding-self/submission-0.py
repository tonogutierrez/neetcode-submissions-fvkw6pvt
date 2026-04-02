class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        ans = [0] * len(nums)

        for i in range(len(nums)):
            ans[i] = prefix 
            prefix *= nums[i]
        
        profix = 1
        for i in range(len(nums)-1,-1,-1):
            ans[i] = profix * ans[i]
            profix = profix * nums[i]
        return ans  