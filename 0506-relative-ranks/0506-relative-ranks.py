class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ranked_score=sorted(score,reverse=True)
        nums_dict={n:i+1 for i,n in enumerate(ranked_score)}
        for i,n in enumerate(score):
            score[i]=str(nums_dict[n])
            if score[i]=='1':
                score[i]='Gold Medal'
            elif score[i]=='2':
                score[i]='Silver Medal'
            elif score[i]=='3':
                score[i]='Bronze Medal'
        return score