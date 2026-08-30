class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:  
        left = 0
        right = len(matrix) * len(matrix[0]) - 1
        while left <=  right:
            mid = (left + right) // 2

            row = mid // len(matrix[0])
            col = mid % len(matrix[0])
            if target == matrix[row][col]:
                return True
            elif target > matrix[row][col]:
                left = mid + 1
            else:
                right = mid - 1
            
        return False
            
