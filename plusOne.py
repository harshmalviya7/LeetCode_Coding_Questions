# 66. Plus One
# https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = int("".join([str(i) for i in digits]))
        l = [int(i) for i in str(s + 1)]
        return l

        #         for i in range(len(digits)-1,-1,-1):

        #             if digits[i]!=9 :
        #                 digits[i]+=1
        #                 return digits
        #             digits[i]=0

        #         digits.insert(0,1)

        #return digits
