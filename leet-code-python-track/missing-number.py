class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        k={num for num in nums}
        for i in range(len(nums)+1):
            if i in k:
                continue
            else:
                if i+1 ==len(k):
                    x=i
                    return x
                else:
                    x=i
                    return x
                break