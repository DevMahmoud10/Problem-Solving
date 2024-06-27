class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        g={i:[] for i in range(len(vals))}
        for s,d in edges:
            g[s].append(d)
            g[d].append(s)
        
        res=float('-inf')
        for n in g:
            cur=vals[n]
            min_heap=[]
            
            for nei in g[n]:
                nei_val=vals[nei]
                if nei_val>0:
                    heapq.heappush(min_heap, vals[nei])
                    cur+=nei_val
                if len(min_heap)>k:
                    cur-=heapq.heappop(min_heap)
            
            res=max(res,cur)
        return res
            
            