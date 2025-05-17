# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head==None:
            return None

        last = head
        n=1

        while last.next:
            last=last.next
            n+=1

        k = k%n #this handles k>=n
        if k==0:
            return head

        new_last = head
        temp = n-k-1

        while temp>0:
            new_last = new_last.next
            temp-=1
        
        new_first = new_last.next
        new_last.next = None
        last.next = head
        
        return new_first