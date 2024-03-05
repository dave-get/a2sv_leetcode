class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        lis = set()
        lis.add(())
        nums.sort()
        def set_(i,temp):
            nonlocal lis
            if len(temp):
                lis.add(tuple(temp))
                # print(lis)
            for j in range(i,len(nums)):
                temp.append(nums[j])
                set_(j+1,temp)
                temp.pop()
        set_(0,[])
       
        return lis