class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        contentS = {}
        contentT = {}
        for i in range(len(s)):
            contentS[s[i]] = 1+ contentS.get(s[i],0)
            contentT[t[i]] = 1 + contentT.get(t[i],0)
        for i in contentS:
            if contentS[i] != contentT.get(i,0):
                return False
        return True

        