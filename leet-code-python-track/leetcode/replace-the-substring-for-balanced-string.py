class Solution:
    def balancedString(self, s: str) -> int:
        count = Counter(s)
        change = defaultdict(int)
        for i in range(len(s)):
            if count[s[i]] > len(s)//4:
                change[s[i]] = count[s[i]] - (len(s)//4)
        total_change = sum(change.values())

        count_change = 0 
        ans = len(s)
        left = 0
        right = 0
        if total_change == 0:
            return 0
        while right < len(s):
            if s[right] in change:
                change[s[right]] -=1
        
            while max(change.values()) <= 0:
                ans = min(ans,right - left +1)
                if s[left] in change:
                    change[s[left]] +=1
                left +=1
            right +=1
        return ans