class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        def dfs(i, subset):
            if i >= len(nums):
                if subset:
                    nonlocal res
                    res += 1
                return
            if not subset or all(abs(nums[i] - x) != k for x in subset):
                subset.append(nums[i])
                dfs(i + 1, subset)
                subset.pop()

            dfs(i + 1, subset)

        res = 0
        dfs(0, [])
        return res
