class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        buckets=[0]*(max(heights)+1)
        for h in heights:
            buckets[h]+=1
        
        expected=[]
        for n,c in enumerate(buckets):
            expected.extend([n]*c)
        
        res=0
        for h,e in zip(heights,expected):
            if h!=e:
                res+=1
        return res
        