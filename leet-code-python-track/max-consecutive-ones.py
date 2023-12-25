class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c=0
        m=0
        for i in nums:
            if i!=1:
                m=max(m,c)
                c=0
            else:
                c+=1
        return max(m,c)