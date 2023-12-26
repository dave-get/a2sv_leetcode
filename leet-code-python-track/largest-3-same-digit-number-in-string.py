class Solution:
    def largestGoodInteger(self, num: str) -> str:
        a=0
        b=1                                     
        c=0                                     
        lis=set()                                  
        for i in range(len(num)-1):
            if num[a]==num[b]:
                c+=1
                b+=1
                if c==2:
                    lis.add(num[a:b])
                if b==len(num):
                    break
            else:
                if c==2:
                    lis.add(num[a:b])
                a=b
                b+=1
                c=0
        if len(lis)!=0:
            return max(lis)
        else:
            return ""