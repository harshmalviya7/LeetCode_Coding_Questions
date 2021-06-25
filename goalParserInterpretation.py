# 1678. Goal Parser Interpretation

# https://leetcode.com/problems/goal-parser-interpretation/

class Solution:
    def interpret(self, command: str) -> str:

        return command.replace('()' ,'o').replace('(al)' ,'al')
#         s=""
#         for i in range(len(command)):
#             if command[i]=="G":
#                 s+="G"

#             elif command[i]==")" and command[i-1]=="(":
#                 s+="o"
#             elif command[i]==")" and command[i-1]=="l":
#                 s+="al"

#         return s
