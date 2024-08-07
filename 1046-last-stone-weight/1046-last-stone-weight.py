class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=[-s for s in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            x,y=heapq.heappop(stones),heapq.heappop(stones)
            if x!=y:
                heapq.heappush(stones, x-y)
        return -stones[0] if stones else 0