class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        print(nums)
        ans = 0
        far = float("inf")
        for i in range(len(nums)-2):
            first = nums[i]
            l = i+1
            r = len(nums)-1
            while l < r:
                sum_ = first + nums[l] + nums[r]
                near = abs(target - sum_)
                if near < far:
                    far = near
                    ans = sum_
                if sum_ < target:
                    l +=1
                else:
                    r -=1
        return ans
            