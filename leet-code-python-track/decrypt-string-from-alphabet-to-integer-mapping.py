class Solution:
    def freqAlphabets(self, s: str) -> str:
        out = ""
        i=0
        while(i<len(s)):
            change =""
            x=s[i:i+3]
            if x[-1]=="#":
                change+=x[0]
                change+=x[1]
                y=int(change)
                k=96+y
                val = chr(k)
                out+=val
                i+=3
            else:
                norm=int(s[i])
                val=96+norm
                out+=chr(val)
                i+=1
        return out
