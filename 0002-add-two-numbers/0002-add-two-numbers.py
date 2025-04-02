from typing import Optional

# Use the platform's ListNode class instead of defining your own
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)  # Changed from -1 to 0 for consistency
        curr = dummy
        carry = 0

        while l1 is not None or l2 is not None or carry:
            sum = carry

            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next

            carry = sum // 10  # Carry for next iteration
            curr.next = ListNode(sum % 10)  # Create new node with digit
            curr = curr.next

        return dummy.next  # Skip the dummy node