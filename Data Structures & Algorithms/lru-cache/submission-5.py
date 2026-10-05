import time

class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev, self.next = None, None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {} # key: Node
        self.capacity = capacity
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        node = Node(key, value)
        if key in self.cache:
            self.remove(self.cache[key])
        self.insert(node)
        self.cache[key] = node
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
    
    
    """ Ranjan's first attempt
    def __init__(self, capacity: int):
        self.lru_cache = {} # key: value, timestamp
        self.capacity = capacity
        # self.oldest = float("+infinity")
        self.lru_times = {} # timestamp: key

    def get(self, key: int) -> int:
        epoch_time = time.time()
        if key in self.lru_cache:
            val, ts = self.lru_cache[key]
            self.lru_cache[key] = (val, epoch_time)
            self.lru_times[epoch_time] = key
            del self.lru_times[ts]
            return self.lru_cache[key][0]
        return -1

    def put(self, key: int, value: int) -> None:
        epoch_time = time.time()
        if key in self.lru_cache:
            old_time = self.lru_cache[key][1]
            del self.lru_times[old_time]
        self.lru_cache[key] = (value, epoch_time)
        self.lru_times[epoch_time] = key
        if len(self.lru_cache) > self.capacity:
            oldest_time = min(self.lru_times.keys())
            oldest_key = self.lru_times[oldest_time]
            del self.lru_times[oldest_time]
            del self.lru_cache[oldest_key]
    """