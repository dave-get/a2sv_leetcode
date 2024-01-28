class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        pre = 0
        lis = [0]
        for i in range(len(nums)):
            pre +=nums[i]
            lis.append(pre)
        print(lis)
        for i in range(len(lis)-1):
            if lis[i]  == lis[-1] - lis[i+1]:
                return i
        return -1