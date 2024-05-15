class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        if grid[0][0]==1 or grid[-1][-1]==1:
            return 0
        
        R,C=len(grid),len(grid[0])
        dirs=[(1,0),(-1,0),(0,1),(0,-1)]
        
        q=deque()
        for r in range(R):
            for c in range(C):
                if grid[r][c]==1:
                    q.append((r,c))
                    grid[r][c]=0
                else:
                    grid[r][c]=-1

        visited = set()
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                if (r,c) in visited:
                    continue
                visited.add((r,c))
                for dr,dc in dirs:
                    dr,dc = r+dr,c+dc
                    if 0<=dr<R and 0<=dc<C and grid[dr][dc]==-1:
                        grid[dr][dc] = grid[r][c]+1
                        q.append((dr,dc))
        
        res = grid[0][0]
        visited = set()
        heap = [(-grid[0][0],0,0)] #(dist,x,y)
        while heap:
            dist,r,c = heapq.heappop(heap)
            res = min(res,-dist)
            if (r,c)==(R-1,C-1):
                return res 
            if (r,c) in visited:
                continue
            visited.add((r,c))
            for dr,dc in dirs:
                dr,dc = r+dr,c+dc
                if 0<=dr<R and 0<=dc<C:
                    heapq.heappush(heap,(-grid[dr][dc],dr,dc))
        return res
    