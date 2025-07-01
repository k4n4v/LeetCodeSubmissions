class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str_s = {}
        str_t = {}

        for c in s:
            if c in str_s:
                str_s[c] += 1
            else:
                str_s[c] = 1
    
        for c in t:
            if c in str_t:
                str_t[c] += 1
            else:
                str_t[c] = 1
    
        if str_s == str_t:
            return True
        
        return False
