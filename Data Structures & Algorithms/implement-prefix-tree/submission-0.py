class Node:
    def __init__(self, val:str) -> None:
        self.val = val
        self.children = {}
        self.is_end = False

    def add_child(self, val:str) -> None:
        self.children[val] = Node(val)

    def has_child(self, val) -> bool:
        return val in self.children
    
    def get_child(self, val) -> bool:
        return self.children.get(val)
    
    def is_word_end(self) -> bool:
        return self.is_end
    
    def set_word_end(self) -> None:
        self.is_end = True
    
class PrefixTree:

    def __init__(self):
        self.root = Node("")
        

    def insert(self, word: str) -> None:
        prev_node = self.root
        for c in word:
            if not prev_node.has_child(c):
                prev_node.add_child(c)
            prev_node = prev_node.get_child(c)
        prev_node.set_word_end()


    def search(self, word: str) -> bool:
        prev_node = self.root
        for c in word:
            if not prev_node.has_child(c):
                return False
            prev_node = prev_node.get_child(c)
        return prev_node.is_word_end()
        

    def startsWith(self, prefix: str) -> bool:
        prev_node = self.root
        for c in prefix:
            if not prev_node.has_child(c):
                return False
            prev_node = prev_node.get_child(c)
        return True

        
        