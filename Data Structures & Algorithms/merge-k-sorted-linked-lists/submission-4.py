# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # implement using minheap
        if not lists or len(lists) == 0:
            return None
        
        dummy = ListNode(0)
        tail = dummy
        minheap = []

        for i in range(len(lists)):
            heapq.heappush(minheap, (lists[i].val, i, lists[i])) 


        while minheap:
            val, i, node = heapq.heappop(minheap)    
            tail.next = ListNode(val) # construct the res list
            tail = tail.next
            # take the index and push other list elem
            if node.next:
                heapq.heappush(minheap, (node.next.val, i, node.next))
            

        return dummy.next    

