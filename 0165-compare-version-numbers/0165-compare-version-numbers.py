class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1_list=version1.split('.')
        v2_list=version2.split('.')
        v1_len,v2_len=len(v1_list),len(v2_list)
        max_len=max(v1_len,v2_len)
        for i in range(max_len):
            v1=int(v1_list[i]) if i<v1_len else 0
            v2=int(v2_list[i]) if i<v2_len else 0
            if v1>v2: return 1
            if v1<v2: return -1
        return 0