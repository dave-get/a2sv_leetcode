class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def func(max_val): 
            count = 1
            _sum = 0
            for i in range(len(nums)):
                _sum +=nums[i]
                if _sum > max_val:
                    count += 1
                    _sum = nums[i]
            return count

        left = max(nums)
        right = sum(nums)
        _max = left

        while left <= right:
            mid = (left+right)//2

            if func(mid) <= k:
                _max = mid
                right = mid - 1
            else:
                left = mid + 1
        return _max
            
            
