class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_deque = deque()
        min_deque = deque()
        res = 0
        l=0
        
        for r in range(len(nums)):
            while max_deque and max_deque[-1] < nums[r]:
                max_deque.pop()
            max_deque.append(nums[r])

            while min_deque and min_deque[-1] > nums[r]:
                min_deque.pop()
            min_deque.append(nums[r])

            while max_deque[0] - min_deque[0] > limit:
                if max_deque[0] == nums[l]:
                    max_deque.popleft()
                if min_deque[0] == nums[l]:
                    min_deque.popleft()
                l+=1
            res = max(res, r-l+1)
            
        return res