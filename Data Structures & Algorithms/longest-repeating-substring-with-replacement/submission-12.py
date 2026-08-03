class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxFreq = 0 
        hashFreq = {}
        ans = 0 
        l = 0

        for r in range(len(s)):
            hashFreq[s[r]] = hashFreq.get(s[r],0) + 1
            maxFreq = max(maxFreq, hashFreq[s[r]])

            while r-l+1-maxFreq > k:
                hashFreq[s[l]] -= 1
                l += 1
            ans = max(ans, r-l+1)
        return ans 
