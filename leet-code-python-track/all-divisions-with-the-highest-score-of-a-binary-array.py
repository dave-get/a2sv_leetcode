class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        num_left = []
        num_right = nums.copy()
        lis = {}
        sum_left = 0
        sum_right = num_right.count(1)
        for indx,val in enumerate(nums): 

            sum_ = sum_left + sum_right
            lis[indx] = sum_
            num_left.append(num_right[indx])

            if num_right[indx] == 0:
                sum_left +=1
            if num_right[indx] ==1:
                sum_right -=1
            
        sum_ = sum_left + sum_right
        lis[len(nums)] = sum_ 

        max_ = max(lis.values())
        ans = [key for key,val in lis.items() if val == max_]
        return ans