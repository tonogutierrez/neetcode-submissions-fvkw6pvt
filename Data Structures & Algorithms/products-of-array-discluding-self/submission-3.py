class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = [0] * len(nums)
        prefix = 1

        for i in range(len(nums)):
            arr[i] = prefix
            prefix *= nums[i]
        
        profix = 1
        for i in range(len(nums)-1,-1,-1):
            arr[i] *= profix
            mult1 = arr[i]
            print(f"mult: {mult1}")
            profix *= nums[i]
            mult2 = profix
            print(f"multProfix: {mult2}")
        
        return arr