class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0 
        r = len(height) - 1
        maxRight = height[r]
        maxLeft = height[l]
        ans = 0 

        while l < r:
            if maxLeft < maxRight:
                l += 1
                maxLeft = max(maxLeft,height[l])
                ans += maxLeft - height[l]
            else:
                r -= 1
                maxRight = max(maxRight,height[r])
                ans += maxRight - height[r]
        return ans 