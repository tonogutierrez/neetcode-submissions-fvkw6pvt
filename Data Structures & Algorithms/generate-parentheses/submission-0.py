class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #Only add open paranthesis if open < n
        #only add a closing parenthesis if closed < open
        #valid if open == closed == n 
        res = []
        stack = []

        def backtrack(openN, closeN):
            if openN == closeN == n:
                res.append("".join(stack))
            
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closeN)
                stack.pop()
            
            if closeN < openN:
                stack.append(")")
                backtrack(openN, closeN + 1)
                stack.pop()
        backtrack(0,0)
        return res 