class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        k = goal
        dic = defaultdict(int)
        pref = [0]
        pre = 0
        for i in range(len(nums)):
            pre += nums[i]
            pref.append(pre)
        count =0
        for i in range(len(pref)):
            if pref[i] - k in dic or pref[i] - k == k:
                count += dic[pref[i]-k]
            dic[pref[i]] +=1
            
        return count
