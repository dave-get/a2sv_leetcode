class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        right =len(nums)-1
        left =0
        count = 0
        while right > left:
            check = nums[left] + nums[right]
            if check == k:
                count +=1
                right -=1
                left +=1
            elif check > k:
                right -=1
            else:
                left +=1
        return count 