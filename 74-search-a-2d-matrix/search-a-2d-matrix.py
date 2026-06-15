class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    
        for row in matrix:
            l = 0
            r = len(matrix[0]) - 1

            while l <= r:
                m = (l + r) // 2
                
                if row[m] == target:
                    return True

                if row[m] < target:
                    l = m + 1
                else:
                    r = m - 1

        return False                   