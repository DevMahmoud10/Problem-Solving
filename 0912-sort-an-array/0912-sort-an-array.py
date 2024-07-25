class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        hq=[]
        for n in nums:
            heapq.heappush(hq, n)
        res=[]
        while hq:
            res.append(heapq.heappop(hq))
        return res
            