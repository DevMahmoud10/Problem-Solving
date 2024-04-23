class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1: return [0]

        g={i:[] for i in range(n)}
        for s,d in edges:
            g[s].append(d)
            g[d].append(s)
        
        leaves=deque()
        nodes_degree={node:len(g[node]) for node in g}
        for node in g:
            if nodes_degree[node]==1:
                leaves.append(node)

        while leaves:
            if n<=2:
                return list(leaves)
            for i in range(len(leaves)):
                node=leaves.popleft()
                n-=1
                for nei in g[node]:
                    nodes_degree[nei]-=1
                    if nodes_degree[nei]==1:
                        leaves.append(nei)
        

        
