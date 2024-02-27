class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        c =0
        turn = False
        for char in s:
            if char == "(":
                stack.append(char)
                turn = True
            else:
                if turn:
                    c +=2**len(stack)
                    turn = False
                stack.pop()
        
        return c//2