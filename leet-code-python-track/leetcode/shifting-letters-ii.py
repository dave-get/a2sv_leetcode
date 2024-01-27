class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        lis = [0]*(len(s)+1)
        s_list = list(s)
        for shift in shifts:
            if shift[2] == 1:
                lis[shift[0]] +=1
                lis[shift[1]+1] -=1
            else:
                lis[shift[0]] -=1
                lis[shift[1]+1] +=1
        pre = 0
        for i in range(len(s)+1):
            pre +=lis[i]
            lis[i] = pre

        for i in range(len(s)):
            s_list[i] = chr((ord(s_list[i]) - ord("a") + lis[i])%26+97)
        ans = "".join(s_list)
        return ans



        
        
        
        
        
        
        
        
        
        
        
        
        
        # lis = list(s)
        # for  num in shifts:
        #     if num[2] == 0:
        #         for n in range(num[0],num[1]+1):
        #             if lis[n] == "a":
        #                 lis[n] = "z"
        #             else:
        #                 lis[n] = chr(ord(lis[n])-1)
        #     else:
        #         for n in range(num[0],num[1]+1):
        #             if lis[n] == "z":
        #                 lis[n] = "a"
        #             else:
        #                 lis[n] = chr(ord(lis[n])+1)
        # ans = "".join(lis)
        # return ans





