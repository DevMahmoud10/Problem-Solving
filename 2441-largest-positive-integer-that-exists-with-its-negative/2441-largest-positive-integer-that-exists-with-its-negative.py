class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums_set=set(nums)
        res=-1
        for n in nums_set:
            if n>0 and n>res and -n in nums_set:
                res=n
            elif n<0 and -n>res and -n in nums_set:
                res=-n
        return res