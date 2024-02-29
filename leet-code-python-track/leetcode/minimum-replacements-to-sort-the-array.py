class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        count = 0
        prev = nums[-1]
        for i in range(len(nums)-2,-1,-1):
            if nums[i] > prev:
                num_break = ceil(nums[i]/prev)
                prev = nums[i]//num_break
                count += num_break-1
            else:
                prev = nums[i]
        return count 