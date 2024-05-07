# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        prv,cur=dummy,head
        while cur:
            double=cur.val*2
            if double>=10:
                cur.val=double%10
                prv.val+=1
            else:
                cur.val=double
            prv=cur
            cur=cur.next
        return dummy if dummy.val>0 else dummy.next