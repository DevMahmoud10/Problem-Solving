class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        R,C=len(matrix),len(matrix[0])
        for r in range(R-2,-1,-1):
            for c in range(C):
                left=matrix[r+1][c-1] if c>0 else float('inf')
                mid=matrix[r+1][c]
                right=matrix[r+1][c+1] if c<C-1 else float('inf')
                matrix[r][c]+=min(left,mid,right)
        return min(matrix[0])