class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        lis = set()
        for i in range(len(nums)-2):
            first = nums[i]
            l = i+1
            r = len(nums)-1
            while l < r:
                sum_ = first + nums[l] +nums[r]
                if sum_ == 0:
                    lis.add((first,nums[l],nums[r]))
                    r -=1
                elif sum_ < 0:
                    l+=1
                else:
                    r-=1
        return list(lis)