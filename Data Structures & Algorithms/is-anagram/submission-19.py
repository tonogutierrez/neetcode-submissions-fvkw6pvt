class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hashMapS = {}
        hashMapT = {}

        for i in range(len(s)):
            hashMapS[s[i]] = 1 + hashMapS.get(s[i],0)
            hashMapT[t[i]] = 1 + hashMapT.get(t[i],0)
        
        print(hashMapS)
        for l in hashMapS:
            if hashMapS.get(l) != hashMapT.get(l):
                return False
        return True 
