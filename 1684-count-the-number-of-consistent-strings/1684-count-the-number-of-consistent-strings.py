class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res=0
        allowed_chars=set(allowed)
        for word in words:
            if all(c in allowed_chars for c in word):
                res+=1
        return res
            