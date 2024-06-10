class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        res=0
        buckets=[0]*(max(heights)+1)
        for h in heights:
            buckets[h]+=1
        expected=[]
        for n,c in enumerate(buckets):
            for _ in range(c):
                expected.append(n)
        for i in range(len(heights)):
            if expected[i]!=heights[i]:
                res+=1
        return res
        