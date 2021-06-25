# 28. Implement strStr()
#https://leetcode.com/problems/implement-strstr/


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if needle= ="":
            return 0
        if haystack= ="":
            return -1
        if len(needle ) >len(haystack):
            return -1
        if haystack==needle:
            return 0

        for i in range(len(haystack ) -len(needle ) +1):
            if haystack[i: i +len(needle) ]==needle:
                return i
        return -1





#         if needle in haystack:
#             return haystack.find(needle)
#         else:
#             return -1



#         try:
#             return haystack.index(needle)
#         except:
#             return -1


# return haystack.find(needle)



