class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix) + 1
        cols= len(matrix[0]) + 1
        self.pre_sum =[[0]*cols for i in range(rows)]
        for r in range(1,rows):
            for c in range(1,cols):
                self.pre_sum[r][c] = matrix[r-1][c-1] + self.pre_sum[r-1][c] + self.pre_sum[r][c-1] - self.pre_sum[r-1][c-1]
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = self.pre_sum[row2+1][col2+1] - self.pre_sum[row1][col2+1] - self.pre_sum[row2+1][col1] + self.pre_sum[row1][col1]
        return total


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)