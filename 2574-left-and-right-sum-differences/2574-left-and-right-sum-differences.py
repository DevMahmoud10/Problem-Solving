class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n=len(nums)
        left,right=[0],[0]
        for i in range(n-1):
            left.append(left[-1]+nums[i])
        for i in range(n-1,0,-1):
            right.append(right[-1]+nums[i])
        
        res=[]
        for i in range(n):
            res.append(abs(left[i]-right[n-i-1]))
        return res