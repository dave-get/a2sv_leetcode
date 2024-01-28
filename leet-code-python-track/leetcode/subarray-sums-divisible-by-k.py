class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = [0]*k
        pre = 0
        for num in nums:
            pre +=num%k
            count[pre%k] +=1   
        ans = count[0]
        for i in count:
            ans += (i*(i-1))//2
        return ans  