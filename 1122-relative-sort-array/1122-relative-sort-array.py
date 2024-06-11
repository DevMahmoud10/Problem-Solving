class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counts=[0]*(max(arr1)+1)
        for n in arr1:
            counts[n]+=1
            
        res=[]
        for n in arr2:
            for _ in range(counts[n]):
                res.append(n)
            counts[n]=0
            
        for i in range(len(counts)):
            while counts[i]>0:
                res.append(i)
                counts[i]-=1
        return res
            
            