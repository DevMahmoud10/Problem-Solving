class Solution:
    def reverseParentheses(self, s: str) -> str:
        stk=[]
        for c in s:
            if c!=')':
                stk.append(c)
            else:
                tmp=[]
                while stk[-1]!='(':
                    tmp.append(stk.pop())
                stk.pop()
                stk.extend(tmp)
        return "".join(stk)