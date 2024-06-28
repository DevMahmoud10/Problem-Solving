class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        degree=[0]*n
        for s,d in roads:
            degree[s]+=1
            degree[d]+=1
        res=0
        label=1
        for d in sorted(degree):
            res+=(label*d)
            label+=1
        return res
        
        