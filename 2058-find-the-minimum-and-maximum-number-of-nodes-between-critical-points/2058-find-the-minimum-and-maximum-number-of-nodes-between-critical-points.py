# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        first_ix,last_ix=0,0
        min_diff,max_diff=float('inf'),float('-inf')
        prv,cur,nxt=head,head.next,head.next.next
        i=1
        while nxt:
            if (prv.val>cur.val<nxt.val) or (prv.val<cur.val>nxt.val):
                if first_ix:
                    max_diff=i-first_ix
                    min_diff=min(i-last_ix, min_diff)
                else:
                    first_ix=i
                last_ix=i
            i+=1
            prv,cur,nxt=cur,nxt,nxt.next
        return [min_diff,max_diff] if min_diff!=float('inf') else [-1,-1]
        