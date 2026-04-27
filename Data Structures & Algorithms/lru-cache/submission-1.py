from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.store = OrderedDict()
        

    def get(self, key: int) -> int:
        if key in self.store:
            self.store.move_to_end(key)
        return self.store.get(key, -1)
        

    def put(self, key: int, value: int) -> None:
        self.store[key] = value
        self.store.move_to_end(key)
        if len(self.store) > self.capacity:
            self.store.popitem(last=False)
        
