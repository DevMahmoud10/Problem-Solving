class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(r,c,visited):
            if 0<=r<R and 0<=c<C and grid[r][c]!=0 and (r,c) not in visited:
                visited.add((r,c))
                total=grid[r][c]
                dirs=[(1,0),(-1,0),(0,1),(0,-1)]
                for dr,dc in dirs:
                    total=max(total, grid[r][c]+dfs(r+dr,c+dc,visited))
                visited.remove((r,c))
                return total
            return 0
        
        R,C=len(grid),len(grid[0])
        res=0
        for i in range(R):
            for j in range(C):
                res=max(res, dfs(i,j,set()))
        return res