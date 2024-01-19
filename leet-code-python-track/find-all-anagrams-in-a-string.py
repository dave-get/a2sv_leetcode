from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # lis = []
        # ss=list(set(s))
        # pp=list(set(p))
        # for i in range(len(s)-(len(p)-1)):
        #     count = 0
        #     for j in range(len(pp)):
        #         if p.count(pp[j]) ==  s[i:i+len(p)].count(pp[j]):
        #             count = count+1
        #     if count == len(pp):
        #         lis.append(i)
        # return lis

        find = Counter(p)
        check = Counter(s[0:len(p)])
        left =0
        lis = []
        for right in range(len(p),len(s)):
            if check == find:
                lis.append(left)
            check[s[right]] +=1
            check[s[left]] -=1
            if check[s[left]] ==0:
                del check[s[left]]
            left +=1
        if check == find:
            lis.append(left)
        return lis