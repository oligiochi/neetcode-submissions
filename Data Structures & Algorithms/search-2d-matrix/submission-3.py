class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #return any(target in row for row in matrix)
        if len(matrix)==1:
            if target in matrix[0]:
                return True
            else:
                return False
        centro=len(matrix)//2
        if matrix[centro][0]>target:
            return self.searchMatrix(matrix[:centro], target)
        if matrix[centro][-1]<target:
            return self.searchMatrix(matrix[centro:], target)
        if target in matrix[centro]:
            return True
        else:
            return False