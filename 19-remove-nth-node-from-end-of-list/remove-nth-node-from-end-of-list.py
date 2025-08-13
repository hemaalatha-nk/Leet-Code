# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode()
        dummy.next=head

        k=0
        while dummy:
            dummy=dummy.next
            k+=1
        print(k)

        print(k-n)
        dummy=ListNode()
        dummy.next=head
        for i in range(k-n-1):
            print(dummy.val)
            dummy=dummy.next
        print("change: ", dummy.val)
        if k-n==1:
            dummy.next=head.next
            return dummy.next
            

        dummy.next=dummy.next.next if dummy.next.next else None
        if k==2 and n==1:
            return dummy.next

        return(head)

            





       
