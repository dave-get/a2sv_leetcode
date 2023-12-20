class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        u=2
        m=0
        lcm = 0
        while n!=m:
            if n%2==0:
                lcm=n
                break;
            m = 2*u
            n = n*u
        return lcm

        