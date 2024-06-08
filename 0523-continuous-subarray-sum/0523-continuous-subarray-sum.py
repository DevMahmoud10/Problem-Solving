class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        reminder_map={0:-1} #reminder:index
        total=0
        for i,n in enumerate(nums):
            total+=n
            r=total%k
            if r not in reminder_map:
                reminder_map[r]=i
            elif i-reminder_map[r]>=2:
                return True
        return False