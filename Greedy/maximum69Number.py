# 1323. Maximum 69 Number
# https://leetcode.com/problems/maximum-69-number/
"""
Example 1:

Input: num = 9669
Output: 9969
Explanation:
Changing the first digit results in 6669.
Changing the second digit results in 9969.
Changing the third digit results in 9699.
Changing the fourth digit results in 9666.
The maximum number is 9969.
Example 2:

Input: num = 9996
Output: 9999
Explanation: Changing the last digit 6 to 9 results in the maximum number."""
class Solution:
    def maximum69Number(self, n: int) -> int:

        num = n
        a = 1
        b = 0
        while (n):
            res = n % 10
            if res == 6:
                b = a
            a += 1
            n //= 10
        print(b)
        return num if b == 0 else num + 3 * (10 ** (b - 1))