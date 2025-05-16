# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        curr1 = headA
        curr2 = headB

        #if list is empty
        if curr1 is None or curr2 is None:
            return 0
        
        #if intersection at first node itself
        if curr1==curr2:
            return curr1

        #using these flags so that we don't traverse the lists more than twice
        i=0
        j=0

        while curr1 is not None:
            if curr1.next is None and i==0:
                curr1 = headB
                i=1
            else:
                curr1 = curr1.next
            
            if curr2.next is None and j==0:
                curr2 = headA
                j=1
            else:
                curr2 = curr2.next
            
            if curr1==curr2:
                return curr1
        return 0