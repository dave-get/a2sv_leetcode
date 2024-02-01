class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool: 
        dic = defaultdict(int)
        s = Counter(s1)
        left = right = 0
        if len(s1) > len(s2):
            return False
        while right < len(s1)-1:
            dic[s2[right]] +=1
            right +=1
        while right < len(s2):
            dic[s2[right]] +=1
            if dic == s:
                return True
            else:
                dic[s2[left]] -=1
                if dic[s2[left]] ==0:
                    del dic[s2[left]]
                left +=1
            right +=1
        return False
