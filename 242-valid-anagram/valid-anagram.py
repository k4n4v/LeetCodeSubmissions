class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(s):
            return False
        
        str_s = {}
        str_t = {}

        for c in s:
            if c not in str_s:
                str_s[c] = 1
            else:
                str_s[c] += 1
        
        for c in t:
            if c not in str_t:
                str_t[c] = 1
            else:
                str_t[c] += 1
        
        return str_t == str_s