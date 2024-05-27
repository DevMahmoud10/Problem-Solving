class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        res=0
        counts=Counter(nums)
        for c in counts:
            if counts[c]==2:
                res^=c
        return res
                
                