class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        contentS = {}
        contentT = {}
        for x in range(len(s)):
            contentS[s[x]] = 1 + contentS.get(s[x],0)
            contentT[t[x]] = 1 + contentT.get(t[x],0)
        for i in contentS:
            if contentS[i] != contentT.get(i,0):
                return False
            
        return True