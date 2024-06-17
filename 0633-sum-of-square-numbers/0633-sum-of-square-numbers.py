class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l,r=0,int(sqrt(c))
        while l<=r:
            total=(l**2)+(r**2)
            if total<c:
                l+=1
            elif total>c:
                r-=1
            else:
                return True
        return False