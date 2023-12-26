class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        lis1=[]
        lis2=[]

        k=len(num1)-1
        g=len(num2)-1

        numb = [0,1,2,3,4,5,6,7,8,9]

        for i in range(max(len(num1),len(num2))):
            c=0
            pow1=pow(10,k)
            pow2=pow(10,g)
            for j in range(48,58):
                if i<len(num1):
                    if num1[i]==chr(j):
                        lis1.append(numb[c]*pow1)
                if  i<len(num2):
                    if num2[i]==chr(j):
                        lis2.append(numb[c]*pow2)
                c+=1
            k-=1
            g-=1
        intsum1=sum(lis1)
        intsum2=sum(lis2)
        return f"{intsum1*intsum2}"

