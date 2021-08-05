# 1346. Check If N and Its Double Exist
# https://leetcode.com/problems/check-if-n-and-its-double-exist/
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        d = {j: i for i, j in enumerate(arr)}
        for i in range(len(arr)):
            if 2 * arr[i] in d and d[2 * arr[i]] != i:
                return True
        return False

