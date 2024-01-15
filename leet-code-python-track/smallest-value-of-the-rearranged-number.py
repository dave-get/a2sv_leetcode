class Solution:
    def smallestNumber(self, num: int) -> int:
        copy_num = str(num)
        lis = [num for num in copy_num]
        inc = sorted(lis)
        dic = sorted(lis,reverse = True)
        p = 0
        for i in range(1,len(lis)):
            if inc[p].isalnum() and inc[p]=="0":
                if int(inc[i]) > 0:
                    inc[p],inc[i] = inc[i],inc[p]
                    ans_str = "".join(inc)
                    result = int(ans_str)
                    return result
                    break
            elif lis[p] == "-":
                dic.pop()
                ans_str = "-"+"".join(dic)
                result = int(ans_str)
                return result
                break
            else:
                ans_str = "".join(inc)
                result = int(ans_str)
                return result
                break
        if len(lis)==1:
            return 0