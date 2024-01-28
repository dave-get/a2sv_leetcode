class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        prefix_product = 1
        for i in range(n):
            result[i] *= prefix_product       #1 1 2 6
            prefix_product *= nums[i]    #1 2 6 24
        suffix_product = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix_product       #24 12 8 6
            suffix_product *= nums[i]    #4 12 24 24
        return result
