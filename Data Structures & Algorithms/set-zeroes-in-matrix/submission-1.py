class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Time: O(n*m)
        Space: O(n*m)
        """
        zero_cols = set()
        zero_rows = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zero_cols.add(j)
                    zero_rows.add(i)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if j in zero_cols or i in zero_rows:
                    matrix[i][j] = 0
        
        

        