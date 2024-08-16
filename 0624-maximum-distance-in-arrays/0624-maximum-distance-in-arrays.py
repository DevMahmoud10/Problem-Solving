class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        res, curMin, curMax = 0, float('inf'), float('-inf')
        for arr in arrays:
            res = max(res, max(arr[-1]-curMin, curMax-arr[0]))
            curMin=min(curMin, arr[0])
            curMax=max(curMax, arr[-1])
        return res