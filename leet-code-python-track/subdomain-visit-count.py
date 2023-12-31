class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        ans = {}
        ln = len(cpdomains)
        for i in range(ln):
            sub = cpdomains[i].split()
            if sub[1] in ans:
                ans[sub[1]] +=int(sub[0])
            else:
                ans[sub[1]]=int(sub[0])
                
            sub_1 = sub[1].split(".")
            for i in range(1,len(sub_1)):
                check = ".".join(sub_1[i:])
                if check in ans:
                    ans[check] += int(sub[0])
                else:
                    ans[check] =int(sub[0])
        ans_list = []
        for key,val in ans.items():
            ans_str = ""
            ans_str +=f"{val}" +" "+key
            ans_list.append(ans_str)
        return ans_list
            
