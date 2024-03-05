class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def perm(lis,st):
            nonlocal ans
            if len(lis) == len(nums):
                ans.append(lis[:])
                return 
            for i in range(len(nums)):
                if not nums[i] in st:
                    st.add(nums[i])
                    lis.append(nums[i])
                    perm(lis,st)
                    lis.pop()
                    st.remove(nums[i])
        st = set()
        perm([],st)
        return ans