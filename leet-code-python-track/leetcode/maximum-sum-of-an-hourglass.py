class Solution(object):
    def maxSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)+1
        col = len(grid[0])+1
        pref = [[0]*col for i in range(row)]
        pre = 0
        for i in range(1,row):
            for j in range(1,col):
                pref[i][j] = grid[i-1][j-1] + pref[i][j-1] + pref[i-1][j] - pref[i-1][j-1]
        ans = 0
        print(pref)
        for i in range(2,len(grid)):
            for j in range(2,len(grid[0])):
                ans = max(ans,pref[i+1][j+1]-grid[i-1][j-2] - grid[i-1][j] - pref[i+1][j-2] - pref[i-2][j+1] + pref[i-2][j-2])
                print(pref[i+1][j+1]-grid[i-1][j-2] - grid[i-1][j] - pref[i+1][j-2] - pref[i-2][j])
        return ans