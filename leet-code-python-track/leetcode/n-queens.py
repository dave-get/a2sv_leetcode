class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        diagonal1 = set()
        diagonal2 = set()
        col = set()
        ans = []
        block = [["."]*n for i in range(n)]

        def search(row):
            if row == n:
                c = ["".join(i) for i in block]
                ans.append(c)
                return
            for i in range(n):
                if i in col or (row+i) in diagonal1 or (row-i) in diagonal2 :
                    continue
                diagonal1.add(row+i)
                diagonal2.add(row-i)
                col.add(i)
                block[row][i] = "Q"
                search(row+1)

                diagonal1.remove(row+i)
                diagonal2.remove(row-i)
                col.remove(i)
                block[row][i] = "."
        search(0)
        return ans