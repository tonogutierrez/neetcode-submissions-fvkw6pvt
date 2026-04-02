class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        contentS = {} #letter-value
        contentT = {}
        for i in range(len(s)):
            contentS[s[i]] = 1 + contentS.get(s[i],0)
            contentT[t[i]] = 1 + contentT.get(t[i],0)
        for item in contentS:
            if contentS[item] != contentT.get(item,0):
                return False
        return True 

        