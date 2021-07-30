# 1720. Decode XORed Array
# https://leetcode.com/problems/decode-xored-array/
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        l = [first]

        for i in encoded:
            l.append(l[-1] ^ i)

        print(l)
        return l