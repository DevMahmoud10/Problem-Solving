class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[]
        counts={}
        for n in nums1:
            counts[n]=counts.get(n,0)+1
        for n in nums2:
            if n in counts:
                res.append(n)
                counts[n]-=1
                if counts[n]==0:
                    del counts[n]
        return res