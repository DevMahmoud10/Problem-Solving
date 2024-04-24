class Solution:
    def tribonacci(self, n: int) -> int:
        if n==0: return 0
        a,b,c=0,1,1
        for i in range(n-2):
            next_tri=a+b+c
            a=b
            b=c
            c=next_tri
        return c