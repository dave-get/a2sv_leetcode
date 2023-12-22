class Solution:
    def numberOfMatches(self, n: int) -> int:
        count=0
        for i in range(n):
            if n%2==0:
                m=int(n/2)
                count+=m
                t=n-m
            else:
                m=int((n-1)/2)
                count+=m
                t=n-m
            n=t
        return count
                        

