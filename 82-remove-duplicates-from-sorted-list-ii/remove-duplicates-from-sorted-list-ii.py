# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # dummy=ListNode()
        # dummy.next=cur
        cur=ListNode()
        dummy=cur
   
        # cur.next=dummy.next

        cur1=cur

        h=ListNode()

        if not head:
            return head
        
        while head and head.next:
            if(head.val==head.next.val):
                h=head
                while head and h.val==head.val :
                    head=head.next
                #     print(h.val,head.val)
                # print(head.val)
            else:
                print("cur: ",head.val)
                cur.next=head
                cur=cur.next
                head=head.next
        
        if head and h.val!=head.val:
            print("cur: ",head.val)
            cur.next=head
            cur=cur.next
        else:
            cur.next=None
            
        return dummy.next 


        