class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                if nums[i]==nums[-2]:
                    nums[i+1]=nums[i]
                elif nums[i+2]>nums[i]:
                    nums[i+1]=nums[i+2]
                else:
                    nums[i]=nums[i+1]
                break
        ans=True
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                ans=False
                break
            else:
                ans=True
        return ans