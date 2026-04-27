class Node:
    def __init__(self, key: int, val:int) -> None:
        self.val = val 
        self.key = key
        self.next_node = None
        self.prev = None
    
    def __repr__(self) -> str:
        return f"""
            Node(
                val={self.val}, 
                next_node = {self.next_node.val if self.next_node else None},
                prev = {self.prev.val if self.prev else None},
            )
        """

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dummy = Node(-1, -1)
        self.end = self.dummy
        self.store = {}

    def _remove(self, node: Node) -> None:
        if self.end == node:
            self.end = node.prev
        prev = node.prev 
        nxt = node.next_node
        prev.next_node = nxt
        if nxt:
            nxt.prev = prev

    def _insert(self, node: None) -> None:
        self.end.next_node = node
        node.prev = self.end
        self.end = node
        node.next_node = None

    def get(self, key: int) -> int:
        if key not in self.store:
            return -1

        node = self.store[key]
        self._remove(node)
        self._insert(node)
        return node.val


    def put(self, key: int, value: int) -> None:
        print("put", key, value)
        print(f"{self.store=}")
        if key in self.store:
            node = self.store[key]
            node.val = value
            self._remove(node)
        else:
            node = Node(key, value)
        print("node: ", node)
        self._insert(node)
        self.store[key] = node


        if len(self.store) > self.capacity:
            node = self.dummy.next_node
            self._remove(node)
            del self.store[node.key]
