# 1768. Merge Strings Alternately
# https://leetcode.com/problems/merge-strings-alternately/
"""
Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b
word2:    p   q   r   s
merged: a p b q   r   s
"""
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        n = len(word1)
        m = len(word2)
        s = ""
        while (i < n and j < m):
            s += word1[i] + word2[j]
            i += 1
            j += 1
        while (i < n):
            s += word1[i]
            i += 1
        while (j < m):
            s += word2[j]
            j += 1
        return s
