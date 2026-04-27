class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        Time: O(n*m)
        Space: O(1) exclude return array
        """    
        left = 0
        right = len(matrix[0]) - 1
        top = 0
        bottom = len(matrix) - 1

        res = []
        total_nums = len(matrix) * len(matrix[0])
        while len(res) < total_nums:
            # top left -> right
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1

            if len(res) == total_nums:
                break
            # right top -> bottom
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1
            if len(res) == total_nums:
                break

            # bottom right -> left
            for i in range(right, left - 1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1
            if len(res) == total_nums:
                break

            # left bottom -> top
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
            if len(res) == total_nums:
                break
        return res
