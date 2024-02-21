class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        # for i in range(max(nums)-min(nums)):
        #     for i in range(len(nums)-1):
        #         if nums[i] < nums[i+1]:
        #             nums[i] +=1
        #             nums[i+1] -=1
        # ans = max(nums)
        # return ans
        cur = nums[0]
        pref = 0
        for i in range(len(nums)):
            pref +=nums[i] 
            if nums[i] > cur:
                cur = max(cur,math.ceil(pref/(i+1)))
        return cur