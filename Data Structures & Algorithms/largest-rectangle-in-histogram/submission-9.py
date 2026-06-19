class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        hashMap = [] #index, heights
        maxArea = 0 

        for i, h in enumerate(heights):
                start = i
                while hashMap and h < hashMap[-1][1]:
                        index,height = hashMap.pop()
                        maxArea = max(maxArea, height *(i-index))
                        start = index
                hashMap.append((start,h))

        for i, h in hashMap:
                maxArea = max(maxArea, h*(len(heights) - i))
        return maxArea