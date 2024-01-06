class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        j = len(mat)-1
        sum_ =0
        for i in range(len(mat)):
            sum_ +=mat[i][i]
            print(sum_)
            if len(mat)%2!=0:
                if  j != i:    
                    sum_ +=mat[j][i]
            else:
                sum_ +=mat[j][i]
            j -=1
            print(sum_)
        

        return sum_