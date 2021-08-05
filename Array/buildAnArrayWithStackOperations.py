# 1441. Build an Array With Stack Operations
# https://leetcode.com/problems/build-an-array-with-stack-operations/
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        j = 0
        l = []
        for i in range(1, n + 1):
            # if j==(len(target)):
            #     break
            if target[j] == i:
                l.append("Push")
                j += 1
            else:
                l.append("Push")
                l.append("Pop")
            if i == target[-1]:
                break

        return l

