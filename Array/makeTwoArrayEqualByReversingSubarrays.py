# 1460. Make Two Arrays Equal by Reversing Sub-arrays
# https://leetcode.com/problems/make-two-arrays-equal-by-reversing-sub-arrays/
'''
Example 1:

Input: target = [1,2,3,4], arr = [2,4,1,3]
Output: true
Explanation: You can follow the next steps to convert arr to target:
1- Reverse sub-array [2,4,1], arr becomes [1,4,2,3]
2- Reverse sub-array [4,2], arr becomes [1,2,4,3]
3- Reverse sub-array [4,3], arr becomes [1,2,3,4]
There are multiple ways to convert arr to target, this is not the only way to do so.
Example 2:

Input: target = [7], arr = [7]
Output: true
Explanation: arr is equal to target without any reverses.
'''
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        if target == arr:
            return True
        d = {}
        for i in target:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for j in arr:
            if j in d and d[j] > 0:
                d[j] -= 1
            else:
                return False
        return True
