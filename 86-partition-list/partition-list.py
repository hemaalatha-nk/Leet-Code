# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        gt_head=ListNode()
        gt=gt_head
        lt_head=ListNode()
        lt=lt_head

        while head:
            if head.val>=x:
                gt.next=head
                gt=gt.next
            else:
                lt.next=head
                lt=lt.next
            head=head.next
        
        lt.next=gt_head.next
        gt.next=None
        return lt_head.next
        