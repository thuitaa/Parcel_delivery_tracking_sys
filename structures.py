# Custom Hash Map Node for Chaining Collision Handling
class HashNode:
    def __init__(self, key, value):
        self.key = key       # Parcel ID
        self.value = value   # Parcel Object
        self.next = None     # Pointer to next node in chain

class CustomHashMap:
    def __init__(self, capacity=11):
        self.capacity = capacity
        self.buckets = [None] * capacity
        self.size = 0

    def _hash(self, key):
        # Polynomial rolling-style hash concept for custom implementation
        return abs(hash(key)) % self.capacity

    def put(self, key, value):
        index = self._hash(key)
        head = self.buckets[index]
        
        # Check if key already exists to update it (CRUD: Update)
        curr = head
        while curr:
            if curr.key == key:
                curr.value = value
                return
            curr = curr.next
            
        # Insert at the head of the chain if it's a new key
        new_node = HashNode(key, value)
        new_node.next = head
        self.buckets[index] = new_node
        self.size += 1

    def get(self, key):
        index = self._hash(key)
        curr = self.buckets[index]
        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next
        return None  # Key not found

    def to_list(self):
        # Utility to pull all active values out of the hash map
        items = []
        for bucket in self.buckets:
            curr = bucket
            while curr:
                items.append(curr.value)
                curr = curr.next
        return items


# Custom Queue Node for Linked List Queue
class QueueNode:
    def __init__(self, data):
        self.data = data     # Parcel Object
        self.next = None

class LinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, data):
        new_node = QueueNode(data)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            return None
        temp = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.size -= 1
        return temp.data

    def is_empty(self):
        return self.head is None

    def to_list(self):
        # Traversal to extract elements for display or sorting
        items = []
        curr = self.head
        while curr:
            items.append(curr.data)
            curr = curr.next
        return items