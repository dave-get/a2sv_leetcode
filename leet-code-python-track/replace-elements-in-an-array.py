class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        chn = {}
        for x, y in reversed(operations):
            chn[x] = chn.get(y, y)
            
        for idx, val in enumerate(nums):
            if val in chn:
                nums[idx] = chn[val]
        return nums