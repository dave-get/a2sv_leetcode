class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # left = 0
        # right = 0
        # ans = count = 0
        # dic = defaultdict(int)
        # for i in range(len(nums)):
        #     if nums[right]%2 != 0:
        #         count +=1
        #         dic[right] = right -left+1
        #     if count > k:
        #         while count > k:
        #             if nums[left]%2 != 0:
        #                 count -=1
        #                 left +=1
        #     if count == k:
        #         ans +=1
        #     right +=1
        right ,left = 0,0
        ans = 0 
        odd_cnt = 0
        ans = 0
        cur_sub_cnt = 0
        for right in range(len(nums)):
            
            if nums[right]%2 == 1:
                odd_cnt += 1
                cur_sub_cnt = 0
                
            while odd_cnt == k:
                if nums[left]%2 == 1:
                    odd_cnt -= 1
                cur_sub_cnt += 1
                left += 1
                
            ans += cur_sub_cnt
            
        return ans