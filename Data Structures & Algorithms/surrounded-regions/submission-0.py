class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        time: O(n * m)
        space: O(1)
        """
        
        queue = []
        # find all 'O' on the edge
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (
                    i == 0 or j == 0
                    or i == len(board) - 1
                    or j == len(board[0]) - 1
                ):
                    if board[i][j] == "O":
                        queue.append((i,j))
        
        while queue:
            cur_i, cur_j = queue.pop()
            board[cur_i][cur_j] = "V"
            for next_i, next_j in [
                (cur_i + 1, cur_j),
                (cur_i - 1, cur_j),
                (cur_i, cur_j + 1),
                (cur_i, cur_j - 1),
            ]:
                if (
                    next_i < 0 or next_i == len(board)
                    or next_j < 0 or next_j == len(board[0])
                    or board[next_i][next_j] != "O"
                ):
                    continue
                
                queue.append((next_i, next_j))
                    
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "V":
                    board[i][j] = "O"
        return