class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        dict_ = {}
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i+j in dict_:
                    dict_[i+j].append(mat[i][j])
                else:
                    dict_[i+j] = [mat[i][j]]
        lis = [num for num in dict_.values()] 
        print(lis)
        ans =[] 
        for i in range(len(lis)):
            if i%2 == 0:
                lis[i].reverse()
                ans +=lis[i]
            else:
                ans +=lis[i]
        return ans