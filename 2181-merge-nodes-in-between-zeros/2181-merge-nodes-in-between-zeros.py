# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        left=right=head.next
        while right:
            left=right
            right=right.next
            while right and right.val!=0:
                left.val+=right.val
                right=right.next
            right=right.next
            left.next=right
        return head.next