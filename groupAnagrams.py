

# 49. Group Anagram
# shttps://leetcode.com/problems/group-anagrams/

from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for i in strs:
            d["".join(sorted(i))].append(i)

        return list(d.values())


