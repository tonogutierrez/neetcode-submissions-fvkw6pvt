class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0 
        ans = 0 

        for r in range(len(s)):
            c = s[r]
            while c in seen:
                seen.remove(s[l])
                l += 1
            ans = max(r-l+1,ans)
            seen.add(c)
        return ans 
