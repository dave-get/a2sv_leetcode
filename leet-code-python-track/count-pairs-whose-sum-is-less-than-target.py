class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        print(nums)
        left = 0
        count = 0
        right = len(nums)-1
        ans_sum = 0
        while right > left:
            sum_ = nums[left] + nums[right] 
            if sum_ >= target:
                while sum_ >= target and right > left:
                    right -=1
                    sum_ = nums[left] + nums[right] 
            else:
                ans_sum += len(nums[left:right])
                left +=1
        print(ans_sum)
        return ans_sum

            
