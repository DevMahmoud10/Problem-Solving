class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        maxScore = max(score)
        
        buckets = [0]*(maxScore+1)
        for i in range(n):
            buckets[score[i]] = i+1
            
        res = ['']*n
        rank = 1
        for i in range(maxScore, -1, -1):
            if buckets[i] == 0:
                continue
            actual_index = buckets[i]-1
            if rank == 1:
                res[actual_index] = "Gold Medal"
            elif rank == 2:
                res[actual_index] = "Silver Medal"
            elif rank == 3:
                res[actual_index] = "Bronze Medal"
            else:
                res[actual_index] = str(rank)
            rank += 1
        return res