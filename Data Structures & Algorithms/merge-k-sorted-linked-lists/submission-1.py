# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # min heap method
        minheap = []

        if not lists or len(lists) == 0:
            return None


        # populate all heads of each list with the index
        for i in range(len(lists)):
            heapq.heappush(minheap, (lists[i].val, i))
            lists[i] = lists[i].next
        
        dummy = ListNode(0)
        tail = dummy
        print(minheap)
        while minheap:
            val, index = heapq.heappop(minheap)
            tail.next = ListNode(val)
            tail = tail.next
            if lists[index]:
                print(minheap)
                heapq.heappush(minheap, (lists[index].val, index))
                lists[index] = lists[index].next

        return dummy.next


         

        