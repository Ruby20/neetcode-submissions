class Node: # chaining -> to handle collisions
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    
    def __init__(self, capacity: int):
        self.capacity = capacity # len of the arr
        self.size = 0 # keys
        self.table = [None] * self.capacity

    def hash_function(self, key):
        return key % self.capacity    


    def insert(self, key: int, value: int) -> None:
        index = self.hash_function(key)
        # where to insert 
        # we will append to the end of the list right?
        node = self.table[index]

        if not node:
            self.table[index] = Node(key, value)
            self.size += 1
        else:
            prev = None
            while node:
                if node.key == key: # key exists but value was updated
                    node.value = value # update the value
                    return
                prev, node = node, node.next # node will point to null, hence need prev
            prev.next = Node(key, value)
            self.size += 1

        # check if resize is needed
        if self.size / self.capacity >= 0.5:
            self.resize()


    def get(self, key: int) -> int:
        index = self.hash_function(key)
        node = self.table[index]
        
        # we get the chain of values or a single value?
        while node:
            if node.key == key:
                return node.value
            node = node.next
        return -1        


    def remove(self, key: int) -> bool:
        index = self.hash_function(key)
        node = self.table[index]
        prev = None

        while node:
            if node.key == key:
                if prev:
                    prev.next = node.next
                else:
                    self.table[index] = node.next
                self.size -= 1
                return True    
            prev, node = node, node.next  
        return False          


    def getSize(self) -> int:
        return self.size


    def getCapacity(self) -> int:
        return self.capacity


    def resize(self) -> None:
        # if half of the arr if full, we will double the capacity
        new_capacity = self.capacity * 2
        new_table = [None] * new_capacity # create a new table and copy 

        for node in self.table:
            while node:
                index = node.key % new_capacity # new position 
                if new_table[index] is None:
                    new_table[index] = Node(node.key, node.value)
                else:
                    new_node = new_table[index]
                    while new_node.next:
                        new_node = new_node.next
                    new_node.next = Node(node.key, node.value)
                node = node.next    

        self.capacity = new_capacity
        self.table = new_table        










