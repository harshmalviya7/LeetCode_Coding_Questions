# 763. Partition Labels
# https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = {c: i for i, c in enumerate(s)}

        j = 0
        a = 0
        l = []
        for i in range(len(s)):
            j = max(j, d[s[i]])
            if i == j:
                l.append(i - a + 1)
                a = i + 1
        return l

