class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(r,c):
            if 0<=r<R and 0<=c<C and grid[r][c]!=0:
                val=grid[r][c]
                grid[r][c]=0
                total=val
                dirs=[(1,0),(-1,0),(0,1),(0,-1)]
                for dr,dc in dirs:
                    total=max(total, val+dfs(r+dr,c+dc))
                grid[r][c]=val
                return total
            return 0
        
        R,C=len(grid),len(grid[0])
        res=0
        for i in range(R):
            for j in range(C):
                res=max(res, dfs(i,j))
        return res