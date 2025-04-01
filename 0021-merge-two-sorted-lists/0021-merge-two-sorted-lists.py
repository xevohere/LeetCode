class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        uno = list1
        dos = list2

        dummy = ListNode(-1)
        prev = dummy

        while uno and dos:
            if uno.val<=dos.val:
                prev.next = uno
                uno = uno.next
            else:
                prev.next = dos
                dos = dos.next
            prev = prev.next
        #append all the elements of the remaining linkedd list
        prev.next = uno if uno else dos
        return dummy.next