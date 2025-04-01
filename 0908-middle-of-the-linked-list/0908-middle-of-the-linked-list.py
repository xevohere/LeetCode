# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        count = 0
        while temp is not None:
            count += 1
            temp = temp.next
        
        n = count//2
        
        temp = head
        for _ in range (n):
            temp = temp.next
        return temp

        