# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()  # Dummy node to simplify result list handling
        current = dummy
        carry = 0  # To handle carry-over values

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0  # Get value from l1, or 0 if None
            val2 = l2.val if l2 else 0  # Get value from l2, or 0 if None
            
            total = val1 + val2 + carry  # Sum of two digits + carry
            carry = total // 10  # Carry for next iteration
            current.next = ListNode(total % 10)  # Create new node with remainder

            # Move pointers forward
            current = current.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next  # Return the next node after dummy