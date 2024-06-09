class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        count=0
        l=0
        for r in range(1,len(skills)):
            if skills[l]>skills[r]:
                count+=1
            else:
                count=1
                l=r
            if count==k:
                break
        return l