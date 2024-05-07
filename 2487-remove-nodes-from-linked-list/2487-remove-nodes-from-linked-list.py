# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse_list(node):
            prv,cur=None,node
            while cur:
                nxt=cur.next
                cur.next=prv
                prv=cur
                cur=nxt
            return prv
        
        reversed_head = reverse_list(head)
        cur=reversed_head
        max_val=cur.val
        while cur.next:
            if max_val>cur.next.val:
                cur.next=cur.next.next
            else:
                cur=cur.next
                max_val=cur.val
        return reverse_list(reversed_head)
            
            