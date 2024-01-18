class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = right = 0
        sum_ = 0
        ans = float("inf")
        while right < len(nums):
            sum_ +=nums[right]
            if sum_ >= target:
                while sum_ >=target and left < len(nums):
                    ans = min(ans,right-left+1)
                    sum_ -=nums[left]
                    left +=1
                right +=1
            else:
                right +=1
        if sum(nums) < target:
            return 0
        return ans