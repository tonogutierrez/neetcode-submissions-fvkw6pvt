class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = [] #temp, index
        #[0,0,0,0,0,0,0]
        #[38,36,35,40]

        for i,t in enumerate(temperatures):
            while stack and temperatures[i] > stack[-1][0] :
                stackT, stackI = stack.pop()
                ans[stackI] = i-stackI
            stack.append((t,i))  
        return ans 
