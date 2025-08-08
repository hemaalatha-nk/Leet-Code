# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy=ListNode()
        current=dummy
        carry=0

        while l1 or l2 or carry:

            sum_= (l1.val if l1 else 0 )+ (l2.val if l2 else 0) + carry
            carry= sum_ // 10
            # current.val=sum_%10
            current.next=ListNode(sum_%10)
            current=current.next
            # print(carry)
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
        return dummy.next

        # n1=""
        # n2=""

        # list1=l1
        # list2=l2

        # carry=0

        # while list1!=None or list2!=None:

        #     if list1!=None:
        #         n1=str(list1.val)+n1
        #         list1=list1.next
        #     if list2!=None:
        #         n2=str(list2.val)+n2
        #         list2=list2.next
        

        # n1=str(int(n1)+int(n2))


        # res=ListNode()
        # cur=res

        # for i in range(len(n1),0,-1):
        #     cur.val=int(n1[i-1:i])
        #     if(i!=1):
        #         c1=ListNode()
        #         cur.next=c1
        #         cur=c1
            
            
        # return res




       