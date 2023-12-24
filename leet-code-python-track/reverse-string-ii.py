class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        lis=list(s)
        con=len(s)
        for i in range(0,len(s),2*k):
            lis[i:k+i]=reversed(lis[i:k+i])    
        ans="".join(lis)
        return ans