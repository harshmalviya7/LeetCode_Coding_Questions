# 917. Reverse Only Letters
# https://leetcode.com/problems/reverse-only-letters/
"""Example 1:

Input: s = "ab-cd"
Output: "dc-ba"
Example 2:

Input: s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
Example 3:

Input: s = "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!""""
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        i = 0
        j = len(s) - 1
        s = list(s)
        while (i < j):
            if (i < len(s) and ((s[i] >= "a" and s[i] <= "z") or (s[i] >= "A" and s[i] <= "Z"))):
                if (j >= 0 and ((s[j] >= "a" and s[j] <= "z") or (s[j] >= "A" and s[j] <= "Z"))):
                    s[i], s[j] = s[j], s[i]
                    i += 1
                    j -= 1
                else:
                    j -= 1
            else:
                i += 1
        return "".join(s)



