class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        unique_set = set()
        file_dict = {}
        splited_list = [files.split() for files in paths]
        for i in range(len(splited_list)): 
            for j in range(1,len(splited_list[i])):
                file_ = splited_list[i][j]
                br = file_.index("(")
                unique_set.add(file_[br:])
                
                form = splited_list[i][0]+"/"+file_[:br]
                file_dict[form]=file_[br:]
        ans = []
        for i in unique_set:
            ans_block =[]
            for key,val in file_dict.items():
                if i==val:
                    ans_block.append(key)            
            if len(ans_block)>=2:
                ans.append(ans_block)
        return ans