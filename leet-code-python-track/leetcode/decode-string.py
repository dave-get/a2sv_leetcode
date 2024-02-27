class Solution:
    def decodeString(self, s: str) -> str:
        nums = []
        chars = []
        opening = 0
        for i,ch in enumerate(s):
            opening += ch == "["
            if nums and ch.isnumeric() and len(nums)-1 == opening:
                nums[-1] *= 10
                nums[-1] += int(ch)
            elif ch.isnumeric():
                nums.append(int(ch))
            if ch == "]":
                sub_string = []
                while chars and chars[-1] != "[":
                    sub_string.append(chars.pop())
                chars.pop()
                opening -= 1
                chars.append("".join(sub_string[::-1])*nums.pop())
            elif not ch.isnumeric():
                chars.append(ch)
        return "".join(chars)