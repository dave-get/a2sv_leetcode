class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l =0
        r =0
        ans = sum_ = 0
        s = defaultdict(int)
        while r < len(fruits):
            if len(s) > 2:
                ch = s[fruits[l]]
                while ch > 0:
                    s[fruits[l]] -=1
                    if s[fruits[l]] == 0:
                        ch = 0
                    else:
                        ch = s[fruits[l]]
                        l +=1
                del s[fruits[l]]
                l+=1
            else:
                s[fruits[r]] +=1 
                r +=1    
                if len(s) <= 2:
                    sum_ = sum(s.values())
            ans = max(ans,sum_)   
        return ans