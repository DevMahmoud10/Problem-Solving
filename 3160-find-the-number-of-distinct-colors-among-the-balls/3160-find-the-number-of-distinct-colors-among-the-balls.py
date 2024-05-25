class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        res=[]
        balls,colors={},{}
        used_colors=0
        for b,c in queries:
            if b not in balls: balls[b]=-1
            if c not in colors: colors[c]=0
            if balls[b]!=-1:
                colors[balls[b]]-=1
                if colors[balls[b]]==0:
                    used_colors-=1
            balls[b]=c
            colors[c]+=1
            if colors[c]==1:
                used_colors+=1
            res.append(used_colors)
        return res
    
        