class Solution:
    def maxScore(self, s: str) -> int:
        ls = [int(num) for num in s]     
        total = sum(ls)
        left = 0
        ans = 0
        for i in range(len(ls)-1) :
            if ls[i] ==0:
                left += 1
            
            total -= ls[i]   
            ans = max(ans, left + total)

        return ans
