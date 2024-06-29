class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        def dfs(node):
            if node in visited:
                return memo[node]
            for nei in g[node]:
                visited.union(dfs(nei))
                visited.add(nei)
            memo[node]=visited
            return memo[node]
            
            
        g={i:[] for i in range(n)}
        for s,d in edges:
            g[d].append(s)
        
        res=[]
        memo={}
        for i in range(n):
            visited=set()
            res.append(sorted(dfs(i)))
        return res
        