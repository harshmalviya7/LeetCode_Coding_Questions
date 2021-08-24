# 537. Complex Number Multiplication
# https://leetcode.com/problems/complex-number-multiplication/
class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        a = int(num1.split("+")[0])
        b = int(num1.split("+")[1].split("i")[0])
        c = int(num2.split("+")[0])
        d = int(num2.split("+")[1].split("i")[0])

        return str(a * c - b * d) + "+" + str(b * c + a * d) + "i"


