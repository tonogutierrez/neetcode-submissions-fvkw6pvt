class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0 
        stack = [] #index, height

        for i in range(len(heights)):
            start = i 
            while stack and stack[-1][1] > heights[i]:
                stackI, stackH = stack.pop()
                maxArea = max(maxArea, stackH * (i - stackI))
                start = stackI
            stack.append((start, heights[i]))
        
        for i, h in stack:
            maxArea = max(maxArea,h *(len(heights) - i))
        return maxArea