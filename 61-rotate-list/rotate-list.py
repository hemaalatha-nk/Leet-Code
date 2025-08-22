# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy=head
        prev=None
        first=ListNode()

        l=0
        while dummy:
            l+=1
            dummy=dummy.next
        dummy=head

        if(k>0 and l>0):
            k=k%l

        if dummy and dummy.next:
            for i in range(k):
                while dummy.next:
                    prev=dummy
                    dummy=dummy.next
                    if dummy.next==None:
                        prev.next=None


                first.next= dummy
                first.next.next=head
                head=first.next

        return(head)
