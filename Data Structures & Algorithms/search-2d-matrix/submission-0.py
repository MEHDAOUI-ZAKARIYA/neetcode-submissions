class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
         
        for i in range(len(matrix)) :
            n = len(matrix[i])
            L = 0 
            R = n - 1
            while  L <= R :
                M = (L + R) // 2

                if matrix[i][M] == target :
                    return True
                elif target < matrix[i][M] :
                    R = M - 1
                else :
                    L = M + 1
        return False 
            



