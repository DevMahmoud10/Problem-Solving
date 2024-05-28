class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        res=0
        cur_cost=0
        l=0
        for r in range(len(s)):
            cost=abs(ord(s[r])-ord(t[r]))
            cur_cost+=cost
            while cur_cost>maxCost:
                cur_cost-=abs(ord(s[l])-ord(t[l]))
                l+=1
            res=max(r-l+1, res)
        return res