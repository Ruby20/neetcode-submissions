# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedL = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i+1] if (i+1) < len(lists) else None
                mergedL.append(self.mergeLists(list1, list2))
            lists = mergedL
        return lists[0]        






    def mergeLists(self, list1: List[Optional[ListNode]], list2: List[Optional[ListNode]]) :
        head = res = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                res.next = list1
                list1 = list1.next
            else:    
                res.next = list2
                list2 = list2.next
            res = res.next

        res.next = list1 or list2
        return head.next        
        