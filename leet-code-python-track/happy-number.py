class Solution:
    def isHappy(self, n: int) -> bool:
        ans = set()
        happy = n
        ans.add(happy)
        while (happy != 1):
            count = 0 
            happy = str(happy)
            for i in happy:
                count += pow(int(i),2)
            happy = count
            if happy in ans:
                happy = -1
                return False
                break
            ans.add(count) 
        
        return True

