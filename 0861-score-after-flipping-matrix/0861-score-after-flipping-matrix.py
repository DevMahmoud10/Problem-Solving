class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        R,C=len(grid),len(grid[0])
        
        #flip rows
        for r in range(R):
            for c in range(C):
                if grid[r][0]==0:
                    for c in range(C):
                        grid[r][c]=0 if grid[r][c]==1 else 1
        
        #flip columns
        for c in range(C):
            ones=0
            for r in range(R):
                ones+=1 if grid[r][c]==1 else 0
            if ones<R/2:
                for r in range(R):
                    grid[r][c]=0 if grid[r][c]==1 else 1
        
        #calculate score
        res=0
        for r in range(R):
            for c in range(C):
                if grid[r][c]==1:
                    res+=2**(C-c-1)
        return res