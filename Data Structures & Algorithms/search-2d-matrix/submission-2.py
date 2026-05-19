class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nrow, ncol = len(matrix), len(matrix[0])

        flat_list = []
        for row in matrix:
            flat_list.extend(row)
        
        print(flat_list)

        start, end = 0, len(flat_list) - 1

        while start <= end:
            mid = (start + end) // 2
            
            if target == flat_list[mid]:
                return True

            elif target > flat_list[mid]:
                start = mid + 1
            else:
                end = mid - 1

        return False