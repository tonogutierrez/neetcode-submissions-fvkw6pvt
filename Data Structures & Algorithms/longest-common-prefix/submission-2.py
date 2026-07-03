class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        firstWord = strs[0]

        for i in range(len(firstWord)):
            letterAct = firstWord[i]

            for palabra in strs:
                if i >= len(palabra) or letterAct != palabra[i]:
                    return res
            res += letterAct
        return res 