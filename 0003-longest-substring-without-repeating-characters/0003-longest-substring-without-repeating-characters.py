class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen=set()
        res,l=0,0
        for r in range(len(s)):
            while s[r] in seen:
                seen.discard(s[l])
                l+=1
            seen.add(s[r])
            res=max(res,r-l+1)
        return res