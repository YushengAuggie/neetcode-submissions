class Node:
    def __init__(self, val):
        self.val = val
        self.children = {} # val: node
        self.is_word = False

    
class Solution:
    def buildTrie(self, root: Node, word:str) -> None:
        prev_node = root
        for w in word:
            if w not in prev_node.children:
                prev_node.children[w] = Node(w)
            prev_node = prev_node.children[w]
        prev_node.is_word = True

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not board[0]:
            return

        def dfs(
            node: Optional[Node], 
            i:int,
            j:int, 
            word:str
        ) -> None:
            if (i, j) in visited or node is None:
                return 

            if node.val != board[i][j]:
                return

            if node.is_word:
                res.add(word + board[i][j])
            
            for row, col in (
                (i + 1, j),
                (i - 1, j),
                (i, j + 1),
                (i, j - 1),
            ):
                if (
                    row < 0 or col < 0 
                    or row == len(board) or col == len(board[0])
                ):
                    continue
                if next_node := node.children.get(board[row][col]):
                    visited.add((i, j))
                    dfs(next_node, row, col, word + board[i][j])
                    visited.remove((i, j))
            return
            
        
        # build Trie from words
        root = Node("")
        for w in words:
            self.buildTrie(root, w)
        
        visited = set()
        res = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(root.children.get(board[i][j]), i, j, "")
        
        return list(res)
        