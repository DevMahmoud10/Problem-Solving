class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        res=0
        l=0
        min_heap,max_heap=[],[]
        
        for r in range(len(nums)):
            heapq.heappush(min_heap, (nums[r],r))
            heapq.heappush(max_heap, (-nums[r],r))
            
            while -max_heap[0][0]-min_heap[0][0]>limit:
                l=1+min(max_heap[0][1], min_heap[0][1])
                
                while max_heap[0][1]<l:
                    heapq.heappop(max_heap)
                while min_heap[0][1]<l:
                    heapq.heappop(min_heap)
            
            res=max(res, r-l+1)
            
        return res
            
            
                
                