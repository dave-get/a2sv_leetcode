class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        outlist = []
        for i in range(n):
            outlist.append(nums[i])
            outlist.append(nums[n + i])
        return outlist
