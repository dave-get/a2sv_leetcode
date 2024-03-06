class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        x = bisect_left(nums,target)
        y = bisect_right(nums,target)
        if x == len(nums) or y == 0:
            return -1,-1
        if nums[x] != target:
            return -1,-1
        return x,y-1