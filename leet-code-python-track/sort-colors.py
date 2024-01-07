class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # red, white, blue = 0, 0, len(nums) - 1

        # while white <= blue:
        #     if nums[white] == 0:
        #         nums[white], nums[red] = nums[red], nums[white]
        #         red += 1
        #         white += 1
        #     elif nums[white] == 1:
        #         white += 1
        #     else:
        #         nums[white], nums[blue] = nums[blue], nums[white]
        #         blue -= 1


        for i in range(1,len(nums)):
            k =i 
            while k>0 and nums[k-1] > nums[k]:
                nums[k],nums[k-1] = nums[k-1],nums[k]
                k -=1