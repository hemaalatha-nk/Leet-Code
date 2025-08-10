# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        dummy =ListNode()
        dummy.next=head
        cur=head
        leftpreNode=dummy


        for i in range(left-1):
            leftpreNode=leftpreNode.next
            cur=cur.next
        
        sublist=cur
        preNode=ListNode()

        for  i in range(right-left+1):
            nextNode=cur.next
            cur.next=preNode
            preNode=cur
            cur=nextNode

        leftpreNode.next=preNode
        sublist.next=cur
        return dummy.next

        