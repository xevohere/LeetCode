# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #creating a temporary pointer to traverse the array
        temp = head

        #creating a stack uing list
        stack = []

        while temp is not None:
            stack.append(temp.val)

            temp = temp.next
        temp = head
        while temp is not None:
            temp.val = stack.pop()

            temp = temp.next
        return head