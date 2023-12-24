class Solution:
    def romanToInt(self, s: str) -> int:
        sm=0
        dic={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000,"IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}
        k=0
        for i in range(0,len(s)):
            val1=dic[s[k]]
            ch=s[k:k+2]
            if ch in dic:
                val2=dic[s[k:k+2]]    
                sm+=val2
                k+=2
            else:
                sm+=val1
                k+=1
                d=0
            if k>=len(s):
                break
        return sm