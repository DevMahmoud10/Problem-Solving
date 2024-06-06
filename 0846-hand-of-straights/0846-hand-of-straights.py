class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize:
            return False
        counts=Counter(hand)
        hq=list(counts.keys())
        heapq.heapify(hq)
        while hq:
            start=hq[0]
            for n in range(start,start+groupSize):
                if n not in counts:
                    return False
                counts[n]-=1
                if counts[n]==0:
                    if n!=hq[0]:
                        return False
                    heapq.heappop(hq)
        return True
            
        