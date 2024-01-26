class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j=0
        for v in nums:
            if v!=val:
                nums[j] = v
                j+=1
        return j
        
        
        # count = 0
        # for i in range(len(nums)):
        #     if nums[i] == val:
        #         nums[i]="_"
        #         count +=1
        #     else:
        #         nums[i] = str(nums[i])
        # nums.sort()
        # for i in range(len(nums)-count):
        #     nums[i] = int(nums[i])
            
        # return len(nums) - count
        
        