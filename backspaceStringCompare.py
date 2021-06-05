# 844. Backspace String Compare
# https://leetcode.com/problems/backspace-string-compare/
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def fun(st):
            a = []
            for i in range(len(st)):
                if st[i] != "#":
                    a.append(st[i])

                elif len(a) != 0:
                    a.pop()
            return a

        return "".join(fun(s)) == "".join(fun(t))


ob = Solution()
print(ob.backspaceCompare("a##c","#a#c"))  #true
