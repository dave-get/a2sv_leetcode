class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        Triangle = [[1]*(i+1) for i in range(rowIndex+1)]
        for row in range(2, rowIndex+1):
            for col in range(1, row):
                Triangle[row][col] = Triangle[row-1][col-1] + Triangle[row-1][col]
        return Triangle[rowIndex]