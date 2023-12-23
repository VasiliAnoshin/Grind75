class Entry:
    def __init__(self, key:int, value:int):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = dict()
        self.left = Entry(0,0)
        self.right = Entry(0,0)
        self.left.next, self.right.prev = self.right, self.left

    def insert(self, node:Entry)->None:
        prev = self.right.prev
        prev.next = node
        node.next = self.right
        self.right.prev = node
        node.prev = prev
       
    def remove(self, node:Entry)->None:
        next_node, prev = node.next, node.prev
        prev.next = next_node
        next_node.prev = prev
       
   
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            node.value = value
            self.insert(node)
        else:
            node = Entry(key, value)
            self.insert(node)
            self.cache[key] = node
            if len(self.cache) > self.size:
                node = self.left.next
                self.remove(node)
                del self.cache[node.key]