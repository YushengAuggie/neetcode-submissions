class Node:
    def __init__(self, val: str):
        self.val = val
        self.children = {}
        self.end_word = False
    
    def has_child(self, val: str) -> bool:
        return val in self.children

    def add_child(self, val: str) -> None:
        self.children[val] = Node(val)

    def get_child(self, val: str) -> Optional[Node]:
        return self.children.get(val)

class WordDictionary:

    def __init__(self):
        self.root = Node("")
        

    def addWord(self, word: str) -> None:
        prev_node = self.root
        for c in word:
            if not prev_node.has_child(c):
                prev_node.add_child(c)
            prev_node = prev_node.get_child(c)
        prev_node.end_word = True


    def search(self, word: str) -> bool:
        def find_next(prev_node: Node, idx:int) -> bool:

            if idx == len(word):
                return prev_node.end_word

            children = prev_node.children
            val = word[idx]

            if val == ".":
                # move to next word
                # try all children
                for val, child in prev_node.children.items():
                    if find_next(child, idx + 1):
                        return True
                return False

            if not val in children:
                return False

            return find_next(children[val], idx + 1)
            
        return find_next(self.root, 0)


        