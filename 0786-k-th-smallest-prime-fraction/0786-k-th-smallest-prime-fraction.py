class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        hq=[]
        for i in range(len(arr)-1):
            for j in range(i+1,len(arr)):
                frc=arr[i]/arr[j]
                heapq.heappush(hq,(-frc,arr[i],arr[j]))
                if len(hq)>k:
                    heapq.heappop(hq)
        f,n,d=heapq.heappop(hq)
        return n,d
            