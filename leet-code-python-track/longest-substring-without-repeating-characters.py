from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = 0
        unique = defaultdict(int)
        ans = 0
        while right < len(s):
            unique[s[right]] +=1
            while unique[s[right]] >1:
                unique[s[left]] -=1
                left +=1
            right +=1
            ans = max(ans,right-left)
        return ans