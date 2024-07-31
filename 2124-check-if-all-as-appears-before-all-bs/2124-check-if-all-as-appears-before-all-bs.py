class Solution:
    def checkString(self, s: str) -> bool:
        max_a,min_b=-1,-1
        for i in range(len(s)):
            if s[i]=='a':
                max_a=i
            elif s[i]=='b' and min_b==-1:
                min_b=i
        return True if (max_a<0 or min_b<0) else max_a<min_b