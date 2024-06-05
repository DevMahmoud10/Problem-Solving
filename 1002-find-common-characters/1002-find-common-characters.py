class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        base_counter=Counter(words[0])
        for i in range(1,len(words)):
            cur_counter=Counter(words[i])
            for c in base_counter:
                base_counter[c]=min(base_counter[c], cur_counter[c])
        res=[]
        for c in base_counter:
            for _ in range(base_counter[c]):
                res.append(c)
        return res