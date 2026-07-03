class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        firstWord = strs[0] #bat, bat, bank

        for i in range(len(firstWord)):
            letraAct = firstWord[i]

            #Comparar la letraAct con las otras
            for palabra in strs:
                if i >= len(palabra) or letraAct != palabra[i]:
                    return res
            res += letraAct
        return res
        
