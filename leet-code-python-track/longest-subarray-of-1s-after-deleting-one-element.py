class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        right = 0
        left = 0
        count_zeros = ans = 0
        while right < len(nums):
            if nums[right] == 0:
                count_zeros +=1
            if count_zeros == 2:
                while count_zeros == 2:
                    if nums[left] == 0:
                        count_zeros -=1
                    left +=1
                right +=1
            else:
                ans = max(ans,right-left)
                right +=1
        return ans