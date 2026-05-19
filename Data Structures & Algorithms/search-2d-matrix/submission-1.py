class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows, cols = len(matrix), len(matrix[0])

        start, end = 0, rows * cols - 1

        while start <= end:
            mid = (start + end) // 2

            # Convert 1D index -> 2D coordinates
            row = mid // cols
            col = mid % cols

            value = matrix[row][col]

            if value == target:
                return True
            elif value < target:
                start = mid + 1
            else:
                end = mid - 1

        return False