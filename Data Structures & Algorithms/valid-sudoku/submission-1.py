from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9
        # check rows
        print("check rows")
        for i in range(N):
            row = set()
            for j in range(N):
                if board[i][j] == ".":
                    continue
                if board[i][j] in row:
                    return False
                row.add(board[i][j])
        
        # check col
        print("check col")
        cols = defaultdict(set)
        for i in range(N):
            for j in range(N):
                if board[i][j] == ".":
                    continue
                if board[i][j] in cols[j]:
                    return False
                cols[j].add(board[i][j])
    
        # check sub-boxes
        # we identy the subbox with i//3, j//3
        print("check subbox")
        subbox = defaultdict(set)
        for i in range(N):
            for j in range(N):
                if board[i][j] == ".":
                    continue
                if board[i][j] in subbox[(i//3, j//3)]:
                    return False
                subbox[(i//3, j//3)].add(board[i][j])

        return True

            

