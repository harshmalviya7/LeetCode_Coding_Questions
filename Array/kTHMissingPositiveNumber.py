# 1539. Kth Missing Positive Number
# https://leetcode.com/problems/kth-missing-positive-number/
Example 1:

Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i = 1
        j = 0
        while (j < len(arr) and k):
            if i == arr[j]:
                i += 1
                j += 1
            else:
                i += 1
                k -= 1
        if k == 0:
            return i - 1
        else:
            return k + i - 1
