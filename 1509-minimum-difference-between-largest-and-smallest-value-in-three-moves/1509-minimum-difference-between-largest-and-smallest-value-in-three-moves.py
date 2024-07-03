class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums)<=4: return 0
        min_four=sorted(heapq.nsmallest(4, nums)) #build heap then return n smallest no need to heapify
        max_four=sorted(heapq.nlargest(4, nums))
        res=float('inf')
        for i in range(4):
            res=min(max_four[i]-min_four[i], res)
        return res
        
    