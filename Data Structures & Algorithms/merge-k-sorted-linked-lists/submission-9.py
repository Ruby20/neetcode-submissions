# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# write a comparator
class NodeComparator:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val    


class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        res = ListNode(0)
        cur = res
        minheap = []

        for lst in lists:
            if lst is not None:
                heapq.heappush(minheap, NodeComparator(lst))

        while minheap:
            node_wrapper = heapq.heappop(minheap)
            cur.next = node_wrapper.node        
            cur = cur.next

            if node_wrapper.node.next:
                heapq.heappush(minheap, NodeComparator(node_wrapper.node.next))

        return res.next    



