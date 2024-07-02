class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        length=len(nums)
        res=[]
        counts={}
        for arr in nums:
            for n in arr:
                counts[n]=counts.get(n,0)+1
        for n in counts:
            if counts[n]==length:
                res.append(n)
        return sorted(res)
        