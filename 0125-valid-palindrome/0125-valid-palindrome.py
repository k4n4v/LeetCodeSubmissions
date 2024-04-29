class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        s_converted = "".join(c for c in s if c.isalnum()).lower()
        
        for i in range(len(s_converted)//2):
            if s_converted[i] == s_converted[len(s_converted)-i-1]:
                continue
            else:
                return False
            
        return True