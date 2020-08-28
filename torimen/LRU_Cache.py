class DoubleLinkedList:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.pre = None
    

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.d = {}
        self.head = DoubleLinkedList('head','head')
        self.tail = DoubleLinkedList('tail','tail')
        self.head.next = self.tail
        self.tail.pre = self.head
        
        
    def get(self, key: int) -> int:
        if key in self.d:
            node = self.d[key]
            self.remove(node)
            self.add(node)
            return node.value
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.remove(self.d[key])
        
        node = DoubleLinkedList(key, value)
        self.add(node)
        self.d[key] = node
        
        if len(self.d) > self.capacity:
            #print(key, value)
            #print(node.pre.value, node.value, node.next.value)
            #print(self.d, self.tail.pre.key)
            node = self.tail.pre
            del self.d[node.key]
            self.remove(node)
    
    def remove(self, node):
        node.pre.next, node.next.pre = node.next, node.pre
        
    def add(self, node):
        next_node = self.head.next #?
        self.head.next, next_node.pre, node.pre, node.next = node, node, self.head, self.head.next
        #print(node.value)
        #print(self.head.next.value, node.pre.value)
        #print(self.tail.pre.value, node.next.value)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
