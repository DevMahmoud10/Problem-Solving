class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        res=0
        hq=[-h for h in happiness]
        heapq.heapify(hq)
        for i in range(k):
            n=-heapq.heappop(hq)
            res+=max(n-i,0)
        return res
            