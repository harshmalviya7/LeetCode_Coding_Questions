# 383. Ransom Note
# https://leetcode.com/problems/ransom-note/
'''
class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        unordered_map<char,int>mp;
        for(auto i:magazine){
            mp[i]++;
        }
        for(auto i :ransomNote){
            if (mp[i]==0){
                return false;
            }
            else{
                mp[i]--;
            }
        }
        return true;
    }
};
'''
from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d=Counter(magazine)
        for i in ransomNote:
            if d[i]==0:
                return False
            else:
                d[i]-=1
        return True