# 1002. Find Common Characters
# https://leetcode.com/problems/find-common-characters/
'''
Example 1:

Input: words = ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: words = ["cool","lock","cook"]
Output: ["c","o"]
'''
from collections import Counter
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if len(words) == 0:
            return []
        if len(words) == 1:
            return list(words[0])

        d1 = Counter(words[0])
        l = []
        for i in d1:
            flag = 0
            count = d1[i]
            for j in range(1, len(words)):
                a = Counter(words[j])
                if i in a:
                    count = min(count, a[i])
                else:
                    flag = 1
                    break
            if not flag:
                l = l + [i] * count

        return l