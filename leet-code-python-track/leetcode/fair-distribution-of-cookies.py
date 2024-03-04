class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        ans = float("inf")
        if k == len(cookies):
            return max(cookies)
        def back_track(i,temp):
            nonlocal ans
            if i == len(cookies):
                ans = min(ans,max(temp[:]))
                return
            for j in range(k):
                temp[j] += cookies[i]
                back_track(i+1,temp)
                temp[j] -=cookies[i]
        temp = [0]*k
        back_track(0,temp)
        return ans