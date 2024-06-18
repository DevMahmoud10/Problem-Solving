class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        worker.sort()
        jobs=sorted(zip(difficulty,profit))
        i,res=0,0
        max_profit=0
        for w in worker:
            while i<len(jobs) and jobs[i][0]<=w:
                max_profit=max(max_profit, jobs[i][1])
                i+=1
            res+=max_profit
        return res