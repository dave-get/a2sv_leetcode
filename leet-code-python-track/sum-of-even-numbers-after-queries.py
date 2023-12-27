class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        S=sum(nums for nums in nums if nums % 2 == 0)
        ans = []

        for x, k in queries:
            if nums[k] % 2 == 0: 
                S -= nums[k]
            nums[k] += x
            if nums[k] % 2 == 0: 
                S += nums[k]
            ans.append(S)
            
        return ans
                