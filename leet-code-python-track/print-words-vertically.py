class Solution:
    def printVertically(self, s: str) -> List[str]:
        k=s.split(" ")
        ma_le=len(max(k,key=len))
        mi_le=len(min(k,key=len))

        lis=[""]*ma_le
        l=0
        for i in range(ma_le):
            for j in range(len(k)):
                if i<len(k[j]):
                    lis[i]+=k[j][i]
                else:
                    lis[i]+=" "
            lis[i]=lis[i].rstrip()
        return lis  

