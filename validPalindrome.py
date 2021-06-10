# 125. Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/


class Solution:
    def isPalindrome(self, s: str) -> bool:

        c=[ch.lower () for ch in s if ch.isalnum()]

        return c==c[::-1]
#          l=0
#         r=len(s)-1

#         while(l<r):
#             while(l<r and (not s[l].isalnum())):

#                 l+=1
#             while(l<r and (not s[r].isalnum())):

#                 r-=1

#             if s[l].lower()==s[r].lower():
#                 l+=1
#                 r-=1
#             else:
#                 return False
#         return True


