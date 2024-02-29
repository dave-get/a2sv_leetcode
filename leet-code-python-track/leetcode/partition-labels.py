class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        lis =defaultdict(int)
        for i in range(len(s)):
            lis[s[i]]=i
        print(lis)
        ans = []
        i = 0
        dif = 0
        while i < len(s):
            n =i
            ma=lis[s[i]]
            while n <= ma:
                if lis[s[n]]>ma:
                    print(i)
                    ma = lis[s[n]]
                n+=1
            ans.append(ma+1 -dif)
            dif = ma+1
            i=n

        return ans