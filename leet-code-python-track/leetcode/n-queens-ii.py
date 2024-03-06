class Solution:
    def totalNQueens(self, n: int) -> int:
        diagonal_dif = set()
        diagonal_sum = set()
        col = set()
        lis = []
        board = [["."]*n for i in range(n)]
        def search(row):
            if row == n:
                ans = ["".join(board[i]) for i in range(n)]
                lis.append(ans)
                return
            for i in range(n):
                if i in col or (row+i) in diagonal_sum or (row-i) in diagonal_dif:
                    continue
                col.add(i)
                diagonal_sum.add(row+i)
                diagonal_dif.add(row-i)
                board[row][i] = "Q"

                search(row+1)
                col.remove(i)
                diagonal_sum.remove(row+i)
                diagonal_dif.remove(row-i)
                board[row][i] = "."
        search(0)
        return len(lis)

