class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list) #key(contador), value(string)
        
        for s in strs:
            count = [0]*26 #a...z
            for c in s:
                count[ord(c)-ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()

        
        