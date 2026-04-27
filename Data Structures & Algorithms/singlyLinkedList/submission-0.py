class Node:
    def __init__(self, val: int):
        self.val = val
        self.next: Node | None = None
    

class LinkedList:
    
    def __init__(self):
        self.root = Node(0)

    
    def get(self, index: int) -> int:
        count = -1
        res = self.root
        """
           r  0 1 2 3
     count -1 0 1 2 3

        """
        while count < index and res:
            res = res.next
            count += 1
        if res:
            return res.val
        else:
            return -1
        

    def insertHead(self, val: int) -> None:
        old_head = self.root.next
        self.root.next = Node(val)
        self.root.next.next = old_head
        

    def insertTail(self, val: int) -> None:
        tail = self.root
        while tail.next:
            tail = tail.next
        tail.next = Node(val)

    def remove(self, index: int) -> bool:
        count = -1
        prev = self.root
        cur = self.root
        while count < index and cur.next:
            prev = cur
            cur = cur.next
            count += 1
        
        if count < index:
            return False
        prev.next = cur.next
        return True
        

    def getValues(self) -> List[int]:
        res = []
        cur = self.root.next
        while cur:
            res.append(cur.val)
            cur = cur.next
        return res
        
