class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        pref = []
        suf = [0]*len(nums)
        pre = 0
        for i in range(len(nums)):
            pref.append(pre) 
            pre +=nums[i]
        sufi =0
        for i in range(len(nums)-1,-1,-1):
            suf[i] = sufi
            sufi +=nums[i]
        n = len(nums)
        ans = []
        for i in range(len(nums)):
            sum_ = abs(pref[i]-(i*nums[i])) + abs(suf[i]-(nums[i]*(n-i-1)))
            ans.append(sum_)
        return ans