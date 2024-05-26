class Solution:
    def checkRecord(self, s: str) -> bool:
        if s.count('A')>=2:
            return False
        late_days=0
        for day in s:
            if day=='L':
                late_days+=1
            else:
                late_days=0
            if late_days==3:
                return False
        return True