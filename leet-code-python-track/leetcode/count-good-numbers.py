class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9+7
        even = ceil(n/2)
        odd = n //2
        res =(pow(5,even,mod)  * pow(4,odd,mod))%mod
        return res