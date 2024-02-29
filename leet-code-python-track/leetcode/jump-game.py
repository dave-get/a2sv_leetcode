class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump = 0
        for index,num in enumerate(nums):
            if index > max_jump:
                return False
            max_jump = max(max_jump,index+num)
        return True 