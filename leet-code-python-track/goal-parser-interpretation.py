class Solution:
    def interpret(self, command: str) -> str:
        h=""
        for i in range(len(command)):
            if command[i]=="G":
                h=h+"G"
            if command[i:i+2]=="()":
                h=h+"o"
            if command[i:i+4]=="(al)":
                h=h+"al"
        return h