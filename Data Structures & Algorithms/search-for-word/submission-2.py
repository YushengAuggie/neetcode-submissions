class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        we could do dfs when hit the word[0]
        and have visited set every time to avoid backward.
        time O(n * 4^m) n is the number of elements of board, and m is the len(word)
        space O(m)
        """
        def dfs(i: int, j: int, board: List[List[str]], word: str, idx:int, visited:set()):
            if idx == len(word):
                return True
            if (
                (i, j) in visited or 
                i == len(board) or 
                j == len(board[0]) or 
                i < 0 or j < 0 or 
                board[i][j] != word[idx]
            ):
                 return False
            print(i, j, board[i][j], idx, word[:idx+1], board[i][j]==word[idx])
            visited.add((i, j))
            for row, col in [
                (-1, 0),
                (0, -1),
                (1, 0),
                (0, 1)
            ]:
                if dfs(i + row, j + col, board, word, idx + 1, visited):
                    return True
            visited.remove((i, j))
            return False
            
        if not board or not word:
            return False

        visited = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, board, word, 0, visited):
                    return True
        return False
