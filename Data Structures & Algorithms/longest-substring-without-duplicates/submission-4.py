class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        best = 0 
        seen = set()

        for r in range(len(s)):
            print(f"before while: {seen}")
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
                print(f"during while: {seen}")
            print(f"after while: {seen}")
            seen.add(s[r])
            best = max(best, r - l + 1)
        return best 