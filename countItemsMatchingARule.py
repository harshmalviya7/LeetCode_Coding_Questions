# https://leetcode.com/problems/count-items-matching-a-rule/
# 1773. Count Items Matching a Rule
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        l = {"type": 0, "color": 1, "name": 2}
        a = 0
        no = l[ruleKey]
        for i in items:
            if ruleValue == i[no]:
                a += 1
        return a
