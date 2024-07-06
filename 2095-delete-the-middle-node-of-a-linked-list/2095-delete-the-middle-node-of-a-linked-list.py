# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        
        prv,slow,fast=None,head,head
        while fast and fast.next:
            prv,slow,fast=slow,slow.next,fast.next.next
            
        prv.next=slow.next
        return head