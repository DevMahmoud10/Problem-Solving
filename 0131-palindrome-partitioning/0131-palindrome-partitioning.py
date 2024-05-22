class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(l,r):
            while l<r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True
            
        def dfs(i,subset):
            if i>=n:
                res.append(subset[:])
                return
            for j in range(i,n):
                if is_palindrome(i,j):
                    subset.append(s[i:j+1])
                    dfs(j+1,subset)
                    subset.pop()
        n=len(s)
        res=[]
        dfs(0,[])
        return res
        