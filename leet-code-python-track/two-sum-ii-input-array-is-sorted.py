class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        while target != numbers[left]+numbers[right]:
            if numbers[left]+numbers[right] < target:
                left +=1
            elif numbers[left]+numbers[right] > target:
                right -=1
            
        ans = [left+1,right+1]
        return ans