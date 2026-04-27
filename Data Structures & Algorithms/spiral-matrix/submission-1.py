class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        Time: O(m * n)
        Space: O(m * n) return
        """
        res = []

        directions = [
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0)
        ]

        visited = set()
        
        def dfs(i: int, j: int, d_idx:int) -> bool:
            if (
                i < 0 or j < 0
                or i > len(matrix) - 1 
                or j > len(matrix[0]) - 1
                or (i, j) in visited
            ):
                # hit
                return False
            print(matrix[i][j])
            res.append(matrix[i][j])
            visited.add((i,j))
            i, j = i + directions[d_idx][0], j + directions[d_idx][1]
            if not dfs(i, j, d_idx):
                print("hit change direction")
                i, j = i - directions[d_idx][0], j - directions[d_idx][1]
                # change direction
                d_idx = (d_idx + 1) % 4
                i, j = i + directions[d_idx][0], j + directions[d_idx][1]
                dfs(i, j, d_idx)
        dfs(0, 0, 0)
        return res

        



        