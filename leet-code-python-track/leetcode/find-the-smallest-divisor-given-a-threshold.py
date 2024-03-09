class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)
        ans = []
        while left <= right:
            mid = (left + right)//2
            _sum = 0
            for i in range(len(nums)):
                _sum += ceil(nums[i]/mid)
            if _sum <= threshold:
                ans.append(mid)
                right = mid -1
            else:
                left = mid +1
        return min(ans)