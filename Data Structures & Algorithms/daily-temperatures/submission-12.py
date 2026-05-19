class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = [] #index, temperature

        for i, x in enumerate(temperatures):
            while stack and temperatures[i] > stack[-1][1]:
                stackI, stackT = stack.pop()
                ans[stackI] = i-stackI
                print(f"dentro del while: {stack}")
            print(f"fuera del while: {stack}")
            stack.append((i,x))
        return ans 