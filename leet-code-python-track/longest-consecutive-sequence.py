class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setnums = set(nums)
        nums = sorted(setnums)
        ans =0
        count =1
        for i in nums:
            if i+1 in setnums:
                count +=1
            else:
                ans=max(ans,count)
                count=1
        if len(nums)==0:
            return 0
        return ans