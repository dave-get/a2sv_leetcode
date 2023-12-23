class Solution:
    def totalMoney(self, n: int) -> int:
        k=1
        count=0
        w=1
        d=7
        for i in range(n):
            if k>d:
                w+=1
                d+=1
                k=w
            count+=k
            k+=1
        return count 
            