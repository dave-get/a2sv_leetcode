class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        left =0
        right =0
        _sum = 0
        ans = 0
        while right < len(nums):
            dic[nums[right]] +=1
            _sum +=nums[right]
            if dic[nums[right]] > 1:
                ans = max(ans,_sum-nums[right])
                while dic[nums[right]] > 1:
                    _sum -=nums[left]
                    dic[nums[left]] -=1
                    left +=1
            right +=1
        ans = max(ans,_sum)
        return ans
                