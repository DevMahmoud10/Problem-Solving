class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        res=[]
        mini=set([min(row) for row in matrix])
        R,C=len(matrix),len(matrix[0])
        for c in range(C):
            col_max=matrix[0][c]
            for r in range(R):
                col_max=max(col_max, matrix[r][c])
            if col_max in mini:
                res.append(col_max)
        return res