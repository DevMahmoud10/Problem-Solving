class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        score, max_score = 0,0
        satisfied=0
        l=0
        for r in range(len(customers)):
            if grumpy[r]==1:
                score+=customers[r]
            else:
                satisfied+=customers[r]
            if r-l+1>minutes:
                if grumpy[l]==1:
                    score-=customers[l]
                l+=1
            max_score=max(score, max_score)
        return satisfied+max_score
                