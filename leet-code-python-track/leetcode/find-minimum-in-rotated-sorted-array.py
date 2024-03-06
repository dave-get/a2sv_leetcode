class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_ = nums[0]

        left = 0
        right = len(nums)-1

        while left < right:
            mid = left + (right-left)//2
            if nums[mid] >= min_:
                left = mid + 1
            elif nums[mid] < min_:
                min_ = nums[mid]
                right = mid - 1 
        if nums[left] < min_:
            return nums[left]
        return min_