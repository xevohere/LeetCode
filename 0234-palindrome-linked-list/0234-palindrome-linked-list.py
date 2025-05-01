# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        pos = head
        stack = []

        while pos:
            stack.append(pos.val)
            pos = pos.next
        
        pos = head
        while pos: 
            if pos.val==stack.pop():
                pos=pos.next
            else:
                return False
        return True
        
        
