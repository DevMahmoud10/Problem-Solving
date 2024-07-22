class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        hq=[(-h,n) for n,h in zip(names,heights)]
        heapq.heapify(hq)
        res=[]
        while hq:
            res.append(heapq.heappop(hq)[1])
        return res