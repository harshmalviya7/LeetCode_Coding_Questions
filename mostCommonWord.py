# 819. Most Common Word
# https://leetcode.com/problems/most-common-word/
import re
import collections
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragrap h =re.sub(r'[^\w\s]+' ," " ,paragraph).split() d=collecti ons.defaultdict(int)
        a=0
        for i in paragraph:
            if i.lower() not in banned:

                d[i.lower()]+=1

                if d[i.lower()]>a:
                    s=i.lower ( )
                    a=d[i.low e r()]


        return s



