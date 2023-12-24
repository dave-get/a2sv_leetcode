class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)+1):
            if i in nums:
                continue
            else:
                if i+1 ==len(nums):
                    x=i
                    return x
                else:
                    x=i
                    return x
                break