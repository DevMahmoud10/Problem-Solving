class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        res=0
        freq=Counter(nums)
        for i in range(len(nums)+max(nums)):
            if freq[i]>1:
                extra=freq[i]-1
                freq[i+1]+=extra
                res+=extra
        return res