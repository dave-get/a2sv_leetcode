class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_ ={}
        for i in range(len(nums)):
            val = target - nums[i]
            if val in dict_:
                return [i,dict_[val]]
            else:
                dict_[nums[i]] = i