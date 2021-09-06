# 1629. Slowest Key
# https://leetcode.com/problems/slowest-key/
class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        if releaseTimes is None:
            return ""
        a = releaseTimes[0]
        c = 0
        for i in range(1, len(releaseTimes)):
            if releaseTimes[i] - releaseTimes[i - 1] >= a:

                if releaseTimes[i] - releaseTimes[i - 1] == a and keysPressed[i] > keysPressed[c]:

                    c = i
                    continue
                elif releaseTimes[i] - releaseTimes[i - 1] == a and keysPressed[i] < keysPressed[c]:
                    continue
                a = releaseTimes[i] - releaseTimes[i - 1]
                c = i
        return keysPressed[c]