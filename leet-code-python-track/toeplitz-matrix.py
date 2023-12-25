class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        t=False
        for j in range(len(matrix)-1):
            if matrix[j][0:-1]==matrix[j+1][1:]:
                t=True
            else:
                return False
        if t:
            return True
        return True