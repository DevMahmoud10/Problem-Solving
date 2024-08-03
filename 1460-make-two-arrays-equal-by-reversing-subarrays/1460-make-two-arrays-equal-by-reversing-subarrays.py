class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        counts=Counter(target)
        for c in arr:
            if c not in counts:
                return False
            counts[c]-=1
            if counts[c]==0:
                del counts[c]
        return not counts