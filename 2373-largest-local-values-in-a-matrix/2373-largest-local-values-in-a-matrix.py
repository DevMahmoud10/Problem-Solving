class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        def get_max(r,c):
            local_max=0
            for i in range(r,r+3):
                for j in range(c,c+3):
                    local_max=max(local_max, grid[i][j])
            return local_max
        
        n=len(grid)
        res=[[0] * (n-2) for _ in range(n-2)]
        for i in range(n-2):
            for j in range(n-2):
                res[i][j]=get_max(i,j)
        return res