class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res=0
        for record in details:
            if int(record[11:13])>60:
                res+=1
        return res