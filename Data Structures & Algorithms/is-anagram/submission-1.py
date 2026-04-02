class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS, countT = {}, {}
        #hay que crear un diccionario
        #racecar 
        #carrace
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0)
            countT[t[i]] = 1 + countT.get(t[i],0)
        for w in countS:
            if countS[w] != countT.get(w,0):
                return False
        return True 