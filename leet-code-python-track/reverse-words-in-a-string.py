class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.lstrip()
        s = s.rstrip()
        copy_splited = s.split()
        
        reverse_splited = reversed(copy_splited)
        
        join_reversed = " ".join(reverse_splited)
        return join_reversed