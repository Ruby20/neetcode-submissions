# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # L and R Two pointer technique
        # start L from Dummy Node
        dummy = ListNode(0, head)
        left = dummy
        right = head
        
        # move right ptr n steps
        while n > 0 and right:
            right = right.next
            n -= 1

        while right: # move both left n right until right meets null
            left = left.next
            right = right.next

        left.next = left.next.next

        return dummy.next        

        