class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s_converted = ""
        
        for c in s:
            if c.isalnum():
                s_converted += c
            
        s_converted = s_converted.lower()
        
        for i in range(len(s_converted)//2):
            if s_converted[i] != s_converted[len(s_converted)-i-1]:
                return False
            
        return True