import bisect
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        use binary search -> row
        and binary search -> whether target in the row
        O(log(m*n))
        """

        # find row
        start = 0
        end = len(matrix) - 1

        row = None
        while start <= end:
            mid = (start + end) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                row = matrix[mid]
                break
            elif matrix[mid][0] > target:
                end = mid - 1
            else:
                start = mid + 1
        if not row:
            return False
        print(row)
        
        idx = bisect.bisect_left(row, target)
        print(idx)
        if idx < len(matrix[0]) and row[idx] == target:
            return True
        return False
        
        
