# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stk=[]
        cur=head
        while cur:
            while stk and cur.val>stk[-1]:
                stk.pop()
            stk.append(cur.val)
            cur=cur.next
            
        dummy=ListNode(0)
        cur=dummy
        for val in stk:
            cur.next=ListNode(val)
            cur=cur.next
        return dummy.next