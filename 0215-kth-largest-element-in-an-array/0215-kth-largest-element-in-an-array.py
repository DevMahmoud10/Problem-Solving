class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hq=[]
        for n in nums:
            heapq.heappush(hq,n)
            while len(hq)>k:
                heapq.heappop(hq)
        return hq[0]