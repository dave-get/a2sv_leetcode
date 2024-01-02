class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        # dict_ = {}
        # count = 0
        # for idx,val in enumerate(nums):
        #     keys = dict_.keys()
        #     if val in dict_.values():
        #         for key in keys:
        #             if key[0] == val:
        #                 if (key[1] * idx)%k == 0:
        #                     count += 1
        #         dict_[val,idx]= val
        #     else:
        #         dict_[val,idx]= val
        # return count

        # count = 0
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i==j:
        #             continue
        #         elif nums[i]==nums[j] and (i*j)%k==0:
        #             print(i,j)
        #             count +=1 
        # return count//2

        count = 0

        for i in range(len(nums)):
            for j in range(len(nums)):
                if 0 <= i and i < j and nums[i] == nums[j] and (i * j) % k == 0:
                    count += 1
        
        return count