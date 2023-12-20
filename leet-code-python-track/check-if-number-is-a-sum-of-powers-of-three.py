class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while(n>0):
            if n%3 != 1 and n%3 != 0:
                x=False
                break
            else:
                x=True
            n=n//3
        return x

            