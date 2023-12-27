class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win = {num[0]:0 for num in matches}
        los = {num[1]:0 for num in matches}

        lis_win=[]
        lis_los=[]
        for x,y in matches:
            if y in win:
                win[y]+=1
            if y in los:
                los[y]+=1
        for w in win:
            if win[w]==0:
                lis_win.append(w)
        for l in los:
            if los[l] ==1:
                lis_los.append(l)
        lis_win.sort()
        lis_los.sort()
        ans=[lis_win] + [lis_los]
        return ans
                