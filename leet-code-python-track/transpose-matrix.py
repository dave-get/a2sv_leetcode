class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        lis = []
        for row in range(len(matrix[0])):
            new = []
            for col in range(len(matrix)):
                new.append(matrix[col][row])
            lis.append(new)
        return lis