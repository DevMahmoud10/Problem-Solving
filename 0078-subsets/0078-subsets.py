class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(i,subset):
            if i>=len(nums):
                res.append(subset[:])
                return
            #apply branching
            #1.append
            subset.append(nums[i])
            dfs(i+1, subset)
            #2.not append
            subset.pop()
            dfs(i+1, subset)

        res=[]
        dfs(0,[])
        return res