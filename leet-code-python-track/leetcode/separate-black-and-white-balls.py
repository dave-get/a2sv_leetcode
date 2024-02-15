class Solution(object):
    def minimumSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        zero = len(s)-1
        one = len(s)-1
        count=0
        lis = list(s)
        for i in range(len(s)):
            if lis[one] == "1" and lis[zero] == "0":
                count += zero - one
                lis[zero],lis[one] = lis[one],lis[zero]
                zero -=1
            elif lis[zero] == "1":
                zero -=1
            one -=1
        return count