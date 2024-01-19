class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum_sub = sum(nums[0:k])
        max_sum = sum_sub
        left = 0
        right = k
        while right < len(nums):
            sum_sub +=nums[right] - nums[left] 
            print(sum_sub)
            max_sum = max(max_sum,sum_sub)
            left +=1
            right +=1
        return max_sum/k