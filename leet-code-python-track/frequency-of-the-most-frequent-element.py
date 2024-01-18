class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        _sum = 0
        right = left = 0
        window = 1
        _max = 0
        pre_sum = 0
        while right < len(nums):
            _sum += nums[right]
            pre_sum =(nums[right]*window) - _sum
            while pre_sum > k:
                _sum -=nums[left]
                left +=1
                window -=1 
                pre_sum =(nums[right]*window) - _sum
            _max = max(_max,window)
            right +=1
            window +=1
            
        return _max