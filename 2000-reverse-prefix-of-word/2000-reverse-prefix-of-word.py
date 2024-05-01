class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        ix=word.find(ch)
        if ix==-1:
            return word
        res=[]
        for i in range(ix,-1,-1):
            res.append(word[i])
        for i in range(ix+1,len(word)):
            res.append(word[i])
        return "".join(res)