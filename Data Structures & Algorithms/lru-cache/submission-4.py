class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        # sentinel/dummy nodes
        # left sentinel finds LRU
        # right sentinel finds MRU
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    # remove node from list
    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    # insert node at right MRU position
    def insert(self, node):
        prev = self.right.prev
        nxt = self.right
        prev.next = node
        node.prev = prev
        nxt.prev = node
        node.next = nxt

    
    def get(self, key: int) -> int:
        if key in self.cache:
            # update the MRU position
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        node = Node(key, value)
        self.cache[key] = node
        self.insert(self.cache[key])
        
        if len(self.cache) > self.capacity:
            # remove/evict the LRU
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]



        
